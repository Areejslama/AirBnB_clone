#!/usr/bin/python3
"""test for city"""

from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class test_User(TestBaseModel):
    """ test user class """

    def __init__(self, *args, **kwargs):
        """init args and kwargs"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_city_id(self):
        """test city value """
        n = self.value()
        self.assertEqual(type(n.state_id), str)

    def test_city_name(self):
        """ test city name """
        n = self.value()
        self.assertEqual(type(n.name), str)
