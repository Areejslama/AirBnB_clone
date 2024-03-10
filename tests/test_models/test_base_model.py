#!/usr/bin/python3
"""Defines unittests for models"""
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModel(unittest.TestCase):
    """testing BaseModel class."""

    def test_no_args_(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_id(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_two_created_at(self):
        b1 = BaseModel()
        sleep(0.05)
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_two_updated_at(self):
        b1 = BaseModel()
        sleep(0.05)
        b2 = BaseModel()
        self.assertLess(b1.updated_at, b2.updated_at)

    def test_str(self):
        my_data = datetime.today()
        my_data_repr = repr(my_data)
        b = BaseModel()
        b.id = "123456"
        b.created_at = b.updated_at = my_data
        bstr = b.__str__()
        self.assertIn("[BaseModel] (123456)", bstr)
        self.assertIn("'id': '123456'", bstr)
        self.assertIn("'created_at': " + my_data_repr, bstr)
        self.assertIn("'updated_at': " + my_data_repr, bstr)

    def test_unused_args(self):
        b = BaseModel(None)
        self.assertNotIn(None, b.__dict__.values())

    def test_kwargs(self):
        my_data = datetime.today()
        my_data_iso = my_data.isoformat()
        b = BaseModel(id="345", created_at=my_data_iso, updated_at=my_data_iso)
        self.assertEqual(b.id, "345")
        self.assertEqual(b.created_at, my_data)
        self.assertEqual(b.updated_at, my_data)

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_with_args_and_kwargs(self):
        my_data = datetime.today()
        my_data_iso = my_data.isoformat()
        b = BaseModel(
                "12", id="345",
                created_at=my_data_iso,
                updated_at=my_data_iso
                )
        self.assertEqual(b.id, "345")
        self.assertEqual(b.created_at, my_data)
        self.assertEqual(b.updated_at, my_data)


class Test_save_method(unittest.TestCase):
    """testing save method"""

    @classmethod
    def setUp(self):
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

    def test_save(self):
        b = BaseModel()
        sleep(0.05)
        f_updated_at = b.updated_at
        b.save()
        self.assertLess(f_updated_at, b.updated_at)

    def test_two_save_methods(self):
        b = BaseModel()
        sleep(0.05)
        f_updated_at = b.updated_at
        b.save()
        s_updated_at = b.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.05)
        b.save()
        self.assertLess(s_updated_at, b.updated_at)

    def test_save_method_with_arg(self):
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.save(None)

    def test_save_update(self):
        b = BaseModel()
        b.save()
        bid = "BaseModel." + b.id
        with open("file.json", "r") as f:
            self.assertIn(bid, f.read())


class Test_to_dict_method(unittest.TestCase):
    """testing to_dict method"""

    def test_to_dict_type(self):
        b = BaseModel()
        self.assertTrue(dict, type(b.to_dict()))

    def test_to_dict_with_keys(self):
        b = BaseModel()
        self.assertIn("id", b.to_dict())
        self.assertIn("created_at", b.to_dict())
        self.assertIn("updated_at", b.to_dict())
        self.assertIn("__class__", b.to_dict())

    def test_to_dict_contains_added_attributes(self):
        b = BaseModel()
        b.name = "school"
        b.my_number = 99
        self.assertIn("name", b.to_dict())
        self.assertIn("my_number", b.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertEqual(str, type(b_dict["created_at"]))
        self.assertEqual(str, type(b_dict["updated_at"]))

    def test_dict_output(self):
        my_data = datetime.today()
        b = BaseModel()
        b.id = "123456"
        b.created_at = b.updated_at = my_data
        mdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': my_data.isoformat(),
            'updated_at': my_data.isoformat()
        }
        self.assertDictEqual(b.to_dict(), mdict)

    def test_contrast_to_dict(self):
        b = BaseModel()
        self.assertNotEqual(b.to_dict(), b.__dict__)

    def test_to_dict_with_arg(self):
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.to_dict(None)


if __name__ == "__main__":
    unittest.main()
