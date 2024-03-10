#!/usr/bin/python3
"""test for user"""

from models.user import User
from tests.test_models.test_base_model import TestBaseModel


class test_User(TestBaseModel):
    """ test user class """

    def __init__(self, *args, **kwargs):
        """init args and kwargs"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

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
