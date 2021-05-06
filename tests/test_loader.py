from unittest import TestCase
import numpy as np
from array2csv.loader import Loader


class TestLoader(TestCase):

    def test_load_file(self):
        """
        Tests if the loader can parse an example input file
        :return: None
        """
        loader = Loader('./tests/example.npz')
        loader.load_file()
        self.assertIsNotNone(loader.data)

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

    def test_get_data(self):
        """
        Test if the loader can return the data
        :return: None
        """
        loader = Loader('')
        loader.data = [0, 1, 2]
        self.assertEqual(loader.get_data(), [0, 1, 2])

    def test_create_aggregated_data(self):
        """
        Tests if the loader can aggregated data using a window size
        :return: None
        """
        loader = Loader('')
        loader.data = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        expected = np.array([[2, 3.5], [6.5, 8]])
        self.assertEqual(loader.create_tiled_data(2).all(), expected.all())
        loader.data = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
        expected = np.array([[2.5, 4.5], [10.5, 12.5]])
        self.assertEqual(loader.create_tiled_data(2).all(), expected.all())
