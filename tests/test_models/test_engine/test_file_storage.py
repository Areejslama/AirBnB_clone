#!/usr/bin/python3
"""Defines unittests"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
import json
import models
import unittest
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """testing methods of FileStorage"""

    @classmethod
    def set(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    class TestFileStorage(unittest.TestCase):
        """testing of FileStorage class."""

    def test_FileStorage_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_save_method(self):
        b = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()
        models.storage.new(b)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(r)
        models.storage.save()
        save_t = ""
        with open("file.json", "r") as fi:
            save_t = fi.read()
            self.assertIn("BaseModel." + b.id, save_t)
            self.assertIn("User." + u.id, save_t)
            self.assertIn("State." + s.id, save_t)
            self.assertIn("Place." + p.id, save_t)
            self.assertIn("City." + c.id, save_t)
            self.assertIn("Amenity." + a.id, save_t)
            self.assertIn("Review." + r.id, save_t)

    def test_save_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_new_method(self):
        b = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()
        models.storage.new(b)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(r)
        self.assertIn("BaseModel." + b.id, models.storage.all().keys())
        self.assertIn(b, models.storage.all().values())
        self.assertIn("User." + u.id, models.storage.all().keys())
        self.assertIn(u, models.storage.all().values())
        self.assertIn("State." + s.id, models.storage.all().keys())
        self.assertIn(s, models.storage.all().values())
        self.assertIn("Place." + p.id, models.storage.all().keys())
        self.assertIn(p, models.storage.all().values())
        self.assertIn("City." + c.id, models.storage.all().keys())
        self.assertIn(c, models.storage.all().values())
        self.assertIn("Amenity." + a.id, models.storage.all().keys())
        self.assertIn(a, models.storage.all().values())
        self.assertIn("Review." + r.id, models.storage.all().keys())
        self.assertIn(r, models.storage.all().values())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_reload(self):
        b = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()
        models.storage.new(b)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(r)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + b.id, obj)
        self.assertIn("User." + u.id, obj)
        self.assertIn("State." + s.id, obj)
        self.assertIn("Place." + p.id, obj)
        self.assertIn("City." + c.id, obj)
        self.assertIn("Amenity." + a.id, obj)
        self.assertIn("Review." + r.id, obj)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)
    
    if __name__ == "__main__":
        unittest.main()

