#!/usr/bin/python3
"""test review """
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel


class test_review(TestBaseModel):
    """test casses """

    def __init__(self, *args, **kwargs):
        """ init args and kwargs """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test place """
        n = self.value()
        self.assertEqual(type(n.place_id), str)

    def test_user_id(self):
        """test user """
        n = self.value()
        self.assertEqual(type(n.user_id), str)

    def test_text(self):
        """test the text """
        n = self.value()
        self.assertEqual(type(n.text), str)
