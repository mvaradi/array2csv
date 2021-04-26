# TODO Add tests

import sys
import ntpath

from numpy import load, amin, amax


class Loader(object):

    def __init__(self, path):
        self.path = path
        self.data = None

    def load_file(self):
        """
        Loads the contents of a compressed .npz file

        The expected input file only has the contents of a single file (i.e. data.files[] has only 1 element)
        That single element is an array with a single embedded array-of-arrays:
        [[[0,1][2,3]]]

        :return: None
        """
        archive = load(self.path)
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
        return amin(self.data), amax(self.data)


# if __name__ == "__main__":
#     loader = Loader(sys.argv[1])
#     loader.load_file()
#
#     # Get data range
#     data_range = loader.get_range()
#     print("Min: %.2f" % data_range[0])
#     print("Max: %.2f" % data_range[1])

