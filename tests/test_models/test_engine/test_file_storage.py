#!/usr/bin/python3
""" unit testing for file storage """
import unittest
from models.engine.file_storage import FileStorage
import pep8

class TestFileStorage(unittest.TestCase):
    """ Test File Storage Class """

    def test_pep8(self):
        """ Test pep8 of files """
        result = pep8.StyleGuide(quiet=True).check_files(
            ['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Found Errors + Warnings")

    def test_class_docstring(self):
        """ Test docstring of Baase Model and its methods """
        self.assertTrue(len(FileStorage.__doc__) >= 1)
        self.assertTrue(len(FileStorage.all.__doc__) >= 1)
        self.assertTrue(len(FileStorage.new.__doc__) >= 1)
        self.assertTrue(len(FileStorage.save.__doc__) >= 1)
        self.assertTrue(len(FileStorage.reload.__doc__) >= 1)