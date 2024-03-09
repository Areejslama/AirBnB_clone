#!/usr/bin/env python3
"""
test for FileStorage
"""
import os
import unittest
import models
import pep8
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Test_Storage(unittest.TestCase):

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "bnb")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("bnb", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """check if all method is working"""

        self.assertIsNotNone(storage.all())
        self.assertEqual(dict, type(storage.all()))
        self.assertIsNotNone(models.engine.file_storage.FileStorage().all)

    def test_new_method(self):
        b = BaseModel()
        storage.new(b)

        self.assertIsNotNone(models.engine.file_storage.FileStorage().new)
        self.assertIn("BaseModel." + b.id, storage.all().keys())
        self.assertIn(b, storage.all().values())

    def test_save(self):
        """check if save method is working"""

        b = BaseModel()
        storage.new(b)
        storage.save()
        with open("file.json", "r") as fi:
            save_t = fi.read()
            self.assertIn("BaseModel." + b.id, save_t)
        self.assertIsNotNone(models.engine.file_storage.FileStorage().save)

    def test_reload(self):
        """check if reload method is working"""
        self.assertIsNotNone(models.engine.file_storage.FileStorage().reload)

    def test_docstring(self):
        """ Test docstring """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_documentation(self):
        """ Test documentation, created and not empty """
        self.assertTrue(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertTrue(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertTrue(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_all(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        o = storage.all()
        self.assertIsNotNone(o)
        self.assertEqual(type(o), dict)
        self.assertIs(o, storage._FileStorage__objects)

    def test_pep8_storage(self):
        """Test that we conform to PEP8."""
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(res.total_errors, 0,
                "Found code style errors (and warnings).")

    if __name__ == '__main__':
        unittest.main()
