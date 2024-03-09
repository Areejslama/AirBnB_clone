#!/usr/bin/python3
"""Unittest for base model module.

This unittest is a collection of possible cases
"""
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
import models
import unittest

class Test_BaseModel(unittest.TestCase):
    """ test instantiation of BaseModel """
    def test_init(self):
        """ test instantiation of BaseModel """
        base_model = BaseModel()
        self.assertEqual(BaseModel, type(BaseModel()))
        self.assertTrue(hasattr(base_model, "id"))

    def test_created_at_instance(self):
        """ test created_at """
        base_model = BaseModel()
        self.assertTrue(isinstance(base_model.created_at, datetime))

    def test_updated_at_instance(self):
        """ test updated_at """
        base_model = BaseModel()
        self.assertTrue(isinstance(base_model.updated_at, datetime))

    def test_created_not_equal(self):
        """ create two objects at different time """
        base_model = BaseModel()
        sleep(0.1)
        base_model_n = BaseModel()
        self.assertNotEqual(base_model.created_at, base_model_n.created_at)

    def test_save_method(self):
        """ Test save method """
        base_model = BaseModel()
        base_model.save()
        self.assertNotEqual(base_model.created_at, base_model.updated_at)

    def test_BaseModel_dict_keys(self):
        """ test to_dict method correct keys """
        base_model = BaseModel()
        data = base_model.to_dict()

        self.assertIn("id", data)
        self.assertIn("created_at", data)
        self.assertIn("updated_at", data)
        self.assertIn("__class__", data)

    def test_BaseModel_str(self):
        """ test str method. assertEqual: a and b are equal"""
        base_model = BaseModel()
        self.assertEqual(type(str(base_model)), str)

    if __name__ == "__main__":
        unittest.main()
