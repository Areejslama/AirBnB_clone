#!/usr/bin/python3
""" test place """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """test place """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Pl"
        self.value = Pl

    def test_city_id(self):
        """test city """
        n = self.value()
        self.assertEqual(type(n.city_id), str)

    def test_user(self):
        """test user """
        n = self.value()
        self.assertEqual(type(n.user_id), str)

    def test_name(self):
        """test name """
        n = self.value()
        self.assertEqual(type(n.name), str)

    def test_description(self):
        """test """
        n = self.value()
        self.assertEqual(type(n.description), str)

    def test_rooms(self):
        """ test rooms """
        n = self.value()
        self.assertEqual(type(n.rooms), int)

    def test_bathrooms(self):
        """test number """
        n = self.value()
        self.assertEqual(type(n.bathrooms), int)

    def test_max_guest(self):
        """test guest """
        n = self.value()
        self.assertEqual(type(n.max_guest), int)

    def test_price_by_night(self):
        """ """
        n = self.value()
        self.assertEqual(type(n.price_by_night), int)

    def test_lati(self):
        """test latuide """
        n = self.value()
        self.assertEqual(type(n.latitude), float)

    def test_long(self):
        """test long"""
        n = self.value()
        self.assertEqual(type(n.latitude), float)

    def test_ids(self):
        """test id """
        n = self.value()
        self.assertEqual(type(n.amenity_ids), list)
