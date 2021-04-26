import os
from unittest import TestCase
from array2csv.writer import Writer


class TestWriter(TestCase):

    def test_get_length(self):
        """
        Test if the writer can get the dimension of the data matrix
        :return: None
        """
        writer = Writer([0, 1, 2], "id")
        self.assertEqual(writer._get_length(), 3)

    def test_save(self):
        """
        Test if the writer correctly writes out the data
        :return: None
        """
        write = Writer([[0, 1], [2, 3]], 'id')
        write.save()
        with open("id_distogram.csv") as tmp:
            content = tmp.read()
            expected = "residueA,residueB,distance\n1,1,0.00\n1,2,1.00\n2,1,2.00\n2,2,3.00\n"
            self.assertEqual(content, expected)
            os.system("rm ./id_distogram.csv")
