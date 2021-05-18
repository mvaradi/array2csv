import os
import json
from unittest import TestCase
from npz_util.writer import Writer


class TestWriter(TestCase):

    def test_turn_to_zero(self):
        """
        Test if the simple transformation works
        :return: None
        """
        writer = Writer([0], "id")
        self.assertEqual(writer.turn_to_zero(19), 19)
        self.assertEqual(writer.turn_to_zero(20), 20)
        self.assertEqual(writer.turn_to_zero(21), 0)

    def test_save_to_csv(self):
        """
        Test if the correct data is getting saved as CSV
        :return: None
        """
        writer = Writer([[1.5, 2.4], [3.6, 4.5]], "tmp")
        writer.save_to_csv()
        tmp = open("tmp_distogram.csv")
        lines = []
        for line in tmp:
            lines.append(line)
        tmp.close()
        self.assertEqual(lines[0], "residue1,residue2,distance\n")
        self.assertEqual(lines[1], "1,1,1.50\n")
        os.system("rm tmp_distogram.csv")
        os.system("del tmp_distogram.csv")

    def test_save_to_tiled_json(self):
        """
        Test if the correct tiled data is saved as JSON
        :return: None
        """
        writer = Writer([[[1.5, 21], [3.6, 22]],[[1.9, 24], [23, 22]]], "tmp")
        writer.save_to_tiled_json()
        tmp = open("tmp_distogram_tiled.json")
        data = json.load(tmp)
        tmp.close()
        expected = [
            {
                "residue1": [1,2],
                "residue2": [1,1],
                "distance": [1.5,3.6]
            },
            {
                "residue1": [1],
                "residue2": [1],
                "distance": [1.9]
            }
        ]
        self.assertEqual(data, expected)
        os.system("rm tmp_distogram_tiled.json")
        os.system("del tmp_distogram_tiled.json")

    def test_save_to_json(self):
        """
        Test if the correct data is getting saved as JSON
        :return: None
        """
        writer = Writer([[1.5, 21], [3.6, 22]], "tmp")
        writer.save_to_json()
        tmp = open("tmp_distogram.json")
        data = json.load(tmp)
        tmp.close()
        expected = [
            {
                "residue1": [1,2],
                "residue2": [1,1],
                "distance": [1.5, 3.6]
            }
        ]
        self.assertEqual(data, expected)
        os.system("rm tmp_distogram.json")
        os.system("del tmp_distogram.json")
