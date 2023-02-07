#!/usr/bin/python3
""" Unit Testing for Base Model """
import unittest
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """ Test Base Model Class """

    def test_pep8(self):
        """ Test pep8 of files """
        result = pep8.StyleGuide(quiet=True).check_files(
            ['models/base_model.py', 'tests/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Found Errors + Warnings")

    def test_class_docstring(self):
        """ Test docstring of Baase Model and its methods """
        self.assertTrue(len(BaseModel.__doc__) >= 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.save.__doc__) >= 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) >= 1)

    def test_str(self):
        my_b = BaseModel()
        d1 = my_b.to_dict()
        self.assertEqual(d1["created_at"], d1["updated_at"])
        my_b.save()
        d1 = my_b.to_dict()
        self.assertNotEqual(d1["created_at"], d1["updated_at"])

if __name__ == "__main__":
    unittest.main()
