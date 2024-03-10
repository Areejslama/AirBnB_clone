#!/usr/bin/python3

"""test for city"""
from models.base_model import BaseModel
from models.city import City


class test_User(test_basemodel):
    """ test user class """

    def __init__(self, *args, **kwargs):
        """init args and kwargs"""
        super().__init__(*args, **kwargs)
        self.name = "Paris"
        self.value = paris
    def test_city_id(self):
        """test city value """
        n = self.value()
        self.assertEqual(type(n.state_id), str)

    def test_city_name(self):
        """ test city name """
        n = self.value()
        self.assertEqual(type(n.name), str)
