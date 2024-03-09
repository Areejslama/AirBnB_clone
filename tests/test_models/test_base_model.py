#!/usr/bin/python3
"""Unittest for base model module.

This unittest is a collection of possible cases
"""
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
import models
import uuid
import unittest

class Test_BaseModel(unittest.TestCase):
    """ test instantiation of BaseModel """
    def test_init(self):
        """ test instantiation of BaseModel """
        b = BaseModel()
        self.assertEqual(BaseModel, type(BaseModel()))
        self.assertTrue(hasattr(b, "id"))

    def test_created_at_instance(self):
        """ test created_at """
        b = BaseModel()
        self.assertTrue(isinstance(b.created_at, datetime))

    def test_updated_at_instance(self):
        """ test updated_at """
        b = BaseModel()
        self.assertTrue(isinstance(b.updated_at, datetime))

    def test_created_not_equal(self):
        """ create two objects at different time """
        b = BaseModel()
        sleep(0.1)
        b_n = BaseModel()
        self.assertNotEqual(b.created_at, b_n.created_at)

    def test_save_method(self):
        """ Test save method """
        b = BaseModel()
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

    def test_dict(self):
        """ test to_dict method correct keys """
        b = BaseModel()
        data = b.to_dict()

        self.assertIn("id", data)
        self.assertIn("created_at", data)
        self.assertIn("updated_at", data)
        self.assertIn("__class__", data)

    def test_BaseModel_str(self):
        """ test str method """
        b = BaseModel()
        self.assertEqual(type(str(b)), str)

    def test_type(self):
        """ test to_dict if contains added attributes """
        b = BaseModel()
        data = b.to_dict()
        self.assertEqual(type(data), dict)

    def test_uuid_format(self):
        """ Tests if UUID  format """
        b = BaseModel()
        self.assertIsInstance(uuid.UUID(b.id), uuid.UUID)

    def test_uuid_wrong_format(self):
        """ Tests a badly UUID """
        b = BaseModel()
        b.id = 'Python'
        w = 'formed hexadecimal string'
        with self.assertRaises(ValueError) as m:
            uuid.UUID(b.id)

    if __name__ == "__main__":
        unittest.main()
