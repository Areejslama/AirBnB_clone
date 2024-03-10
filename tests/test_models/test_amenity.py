#!/usr/bin/python3
"""test case"""
from models.amenity import Amenity
from tests.test_models.test_base_model import test_basemodel


class test_Amenity(test_basemodel):
    """test a class"""

    def __init__(self, *args, **kwargs):
        """ init args and kwargs """
        super().__init__(*args, **kwargs)
        self.name = "A"
        self.value = A

    def test_name(self):
        """test class name"""
        n = self.value()
        self.assertEqual(type(n.name), str)
