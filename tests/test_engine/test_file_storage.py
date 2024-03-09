#!/usr/bin/env python3
""" test for filestorage """
import models
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestStorage(unittest.TestCase):
    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
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
    
    def test_new(self):
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
        with open("file.json", "r") as f:
            save_t = f.read()
            self.assertIn("BaseModel." + b.id, save_t)
            self.assertIsNotNone(models.engine.file_storage.FileStorage().save)
    
    def test_reload(self):
        """check if reload method is working"""
        self.assertIsNotNone(models.engine.file_storage.FileStorage().reload)

    if __name__ == '__main__':
        unittest.main()
