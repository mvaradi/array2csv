import sys
import ntpath

import numpy as np
# from numpy import load, amin, amax, ceil


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

    def get_number_of_iterations(self, window):
        """
        This method calculates the number of iterations required by the create_aggregated_data() method
        :param window: Number, window size
        :return: Number
        """
        dimension = len(self.data)
        number_of_iterations = np.square(np.ceil(dimension / window))
        return number_of_iterations

    def create_aggregated_data(self, window_size):
        """
        This method takes an input n x n numpy array-of-arrays (i.e. matrix) and creates a new matrix
        that has the average or an i x i size slice matrix in a new matrix

        For example:
        input = [[0,1],[2,3]]
        output with a window of 2x2 = [[1.5]]
        :return: Numpy array of arrays
        """

        """
        Get the number of iterations needed to slide a window through the matrix
        The window first moves through a row (from left to right) and then goes
        down and starts again at the beginning of the row
        """
        iterations = self.get_number_of_iterations(window_size)
        x = 0
        y = 0
        data = []
        for i in range(int(iterations)):
            values = []
            values.append(self.data[x][y])
            if y+1 < len(self.data[x]):
                values.append(self.data[x][y+1])
            if x+1 < len(self.data):
                values.append(self.data[x+1][y])
            if x + 1 < len(self.data) and y+1 < len(self.data[x+1]):
                values.append(self.data[x+1][y+1])
            data.append(np.mean(values))

            if y + 2 > len(self.data[x]) - 1:
                if y + 1 > len(self.data[x]) - 1:
                    # The window reached the end of the row, so rewind it to 0
                    y = 0
                    if x + 2 > len(self.data) - 1:
                        if x + 1 > len(self.data) - 1:
                            # The window reached the end of the bottom row, so end the loop
                            break
                        else:
                            x += 1
                    else:
                        x += 2
                else:
                    y += 1
            else:
                y += 2
        return self.make_aggregated_matrix(data, iterations)

    def make_aggregated_matrix(self, data, iterations):
        dimension = int(np.sqrt(iterations))
        return np.array(data).reshape(dimension, dimension)


# if __name__ == "__main__":
#     loader = Loader(sys.argv[1])
#     loader.load_file()
#
#     # Get data range
#     data_range = loader.get_range()
#     print("Min: %.2f" % data_range[0])
#     print("Max: %.2f" % data_range[1])

