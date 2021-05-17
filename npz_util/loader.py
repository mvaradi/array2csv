import ntpath

import numpy as np
from numpy.lib.stride_tricks import as_strided


class Loader(object):
    """
    This class handles .npz data that has an embedded matrix-like object.

    Its methods deal with loading/unpacking Numpy .npz data objects,
    and can also create a tiled data which is averaging values in a window
    of the matrix (i.e. averaging values in a sub-matrix).
    """

    def __init__(self, path):
        self.path = path
        self.data = None
        self.tiled_data = None

    def load_file(self):
        """
        Loads the contents of a compressed .npz file

        The expected input file only has the contents of a single file (i.e. data.files[] has only 1 element)
        That single element is an array with a single embedded array-of-arrays:
        [[[0,1][2,3]]]

        :return: None
        """
        archive = np.load(self.path)
        self.data = archive[archive.files[0]][0]

    def get_data(self):
        """
        Get the data
        :return: Numpy array of arrays
        """
        return self.data

    def get_identifier(self):
        """
        Sets the identifier attribute

        The input file name is expected to be in the format of [identifier]_[*]+.npz
        For example: identifier_example.npz

        :return: None
        """
        return ntpath.basename(self.path).split('_')[0]

    def get_range(self):
        """
        Gets the minimum and maximum values from the data array-of-arrays

        :return: Tuple, min and max values in the data
        """
        return np.amin(self.data), np.amax(self.data)

    def create_tiled_data(self):
        """
        This method takes an input n x n numpy array-of-arrays (i.e. matrix) and creates a new matrix
        that has the average or an i x i size slice matrix in a new matrix

        For example:
        input = [[0,1],[2,3]]
        output with a window of 2x2 = [[1.5]]
        :return: Numpy array of arrays
        """
        data = self.data
        tiled_data = [data]
        while len(data) > 300:
            dimension = data.shape[0]
            if dimension % 2 != 0:
                trimmed_data = data[0:len(data)-1, 0:len(data)-1]
                data = trimmed_data
            data = self.sum_sub_matrices(data, 2)
            tiled_data.append(data)
        self.tiled_data = tiled_data
        return tiled_data

    @staticmethod
    def as_sub_matrices(x, rows, cols=None, writeable=False):
        """
        Create sub-matrices from an input Numpy array-of-arrays (i.e. matrix)
        It uses "rows" and "cols" to set the window size for getting the sub-matrices

        :param x: Numpy array (matrix)
        :param rows: Number; the size of the window in terms of rows
        :param cols: Number; the size of the window in terms of columns
        :param writeable: Boolean
        :return: Numpy array of sub-matrices
        """
        if cols is None:
            cols = rows
        x = np.asarray(x)
        x_rows, x_cols = x.shape
        s1, s2 = x.strides
        if x_rows % rows != 0 or x_cols % cols != 0:
            print(x_rows, rows, x_cols, cols)
            raise ValueError('Invalid dimensions.')
        out_shape = (x_rows // rows, x_cols // cols, rows, cols)
        out_strides = (s1 * rows, s2 * cols, s1, s2)
        return as_strided(x, out_shape, out_strides, writeable=writeable)

    def sum_sub_matrices(self, x, rows, cols=None):
        """
        Calculate the sum over a window in a matrix

        :param x: Numpy array (matrix)
        :param rows: Number; the size of the window in terms of rows
        :param cols: Number; the size of the window in terms of columns
        :return: Numpy array (matrix); same size as x
        """
        if cols is None:
            cols = rows
        x = np.asarray(x)
        x_sub = self.as_sub_matrices(x, rows, cols)
        x_sum = np.mean(x_sub, axis=(2, 3))
        return x_sum
