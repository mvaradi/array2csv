from unittest import TestCase
import numpy as np
from npz_util.loader import Loader


class TestLoader(TestCase):
    def test_load_file(self):
        """
        Tests if the loader can parse an example input file
        :return: None
        """
        loader = Loader('./tests/example.npz')
        loader.load_file()
        self.assertIsNotNone(loader.data)

    def test_get_data(self):
        """
        Test if the loader can return the data
        :return: None
        """
        loader = Loader('')
        loader.data = [0, 1, 2]
        self.assertEqual(loader.get_data(), [0, 1, 2])

    def test_get_identifier(self):
        """
        Test if the loader returns the identifier correctly
        :return: None
        """
        loader = Loader('/path/to/data/identifier_example.npz')
        self.assertEqual(loader.get_identifier(), 'identifier')

    def test_get_range(self):
        """
        Test if the loader can correctly extract the minimum and maximum values from the data
        :return: None
        """
        loader = Loader('./tests/example.npz')
        loader.load_file()
        data_range = loader.get_range()
        print(type(data_range[0]))
        self.assertEqual(np.float16(2.156), data_range[0])
        self.assertEqual(np.float16(21.94), data_range[1])

    def test_create_aggregated_data(self):
        """
        Tests if the loader can aggregated data using a window size
        :return: None
        """
        loader = Loader('')
        loader.data = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        expected = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertEqual(loader.create_tiled_data()[0].all(), expected.all())
        mock_data = np.zeros((301, 301))
        loader.data = mock_data
        loader.sum_submatrices = lambda x, y: np.array([0.5, 2.5])
        self.assertEqual(loader.create_tiled_data()[1].all(), np.array([0.5, 2.5]).all())


    def test_as_submatrices(self):
        """
        Test if the correct strided matrix is returns or if error is raised
        :return: None
        """
        loader = Loader('')
        loader.data = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        expected = np.array([[[[0, 1, 2],
                               [3, 4, 5],
                               [6, 7, 8]]]])
        self.assertEqual(loader.as_submatrices(loader.data, 3).all(), expected.all())
        with self.assertRaises(ValueError):
            loader.as_submatrices(loader.data, 2)

    def test_sum_submatrices(self):
        loader = Loader('')
        loader.data = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        submatrix = np.array([[[[0, 1, 2],
                                [3, 4, 5],
                                [6, 7, 8]]]])
        loader.as_submatrices = lambda x, y, z: submatrix
        self.assertEqual(loader.sum_submatrices(loader.data, 3), 4)
        submatrix = np.array([[[[0, 1, 2],
                                [3, 4, 5],
                                [6, 7, 8]]],
                              [[[1, 1, 1],
                                [1, 3, 3],
                                [2, 3, 3]]]])
        self.assertEqual(loader.sum_submatrices(loader.data, 3).all(), np.asarray([4, 2]).all())
