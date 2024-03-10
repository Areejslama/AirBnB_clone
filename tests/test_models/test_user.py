#!/usr/bin/python3
"""test for user"""
import unittest
from models.user import User
from models.base_model import BaseModel

class test_User(test_basemodel):
    """ test user class """

    def __init__(self, *args, **kwargs):
        """init args and kwargs"""
        super().__init__(*args, **kwargs)
        self.name = "NAME"
        self.value = name

    def test_first(self):
        """ test user firs name """
        n = self.value()
        self.assertEqual(type(n.first_name), str)

    def test_last(self):
        """test user last name """
        n = self.value()
        self.assertEqual(type(n.last_name), str)

    def test_user_email(self):
        """ test email"""
        n = self.value()
        self.assertEqual(type(n.email), str)

    def test_use_password(self):
        """ test user password """
        n = self.value()
        self.assertEqual(type(n.password), str)
