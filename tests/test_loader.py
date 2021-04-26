from unittest import TestCase
import numpy as np
from array2csv.loader import Loader


class TestLoader(TestCase):

    # def setUp(self):
    #     self.loader = Loader('')

    def test_load_file(self):
        """
        Tests if the loader can parse an example input file
        :return: None
        """
        loader = Loader('./tests/example.npz')
        loader.load_file()
        self.assertIsNotNone(loader.data)

    def test_set_identifier(self):
        """
        Test if the loader can process the file path and get the identifier from it
        :return: None
        """
        loader = Loader('path/to/file/identifier_example.npz')
        loader.set_identifier()
        self.assertEqual(loader.identifier, 'identifier')

    def test_get_identifier(self):
        """
        Test if the loader returns the identifier correctly
        :return: None
        """
        loader = Loader('')
        loader.identifier = 'foo'
        self.assertEqual(loader.get_identifier(), 'foo')

    def test_get_range(self):
        """
        Test if the loader can correctly extract the minimum and maximum values from the data
        :return:
        """
        loader = Loader('./tests/example.npz')
        loader.load_file()
        data_range = loader.get_range()
        print(type(data_range[0]))
        self.assertEqual(np.float16(2.156), data_range[0])
        self.assertEqual(np.float16(21.94), data_range[1])