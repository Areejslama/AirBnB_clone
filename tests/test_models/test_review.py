#!/usr/bin/python3
"""test review """
from models.review import Review
from tests.test_models.test_base_model import test_basemodel


class test_review(test_basemodel):
    """test casses """

    def __init__(self, *args, **kwargs):
        """ init args and kwargs """
        super().__init__(*args, **kwargs)
        self.name = "Rev"
        self.value = Rev

    def test_place(self):
        """test place """
        n = self.value()
        self.assertEqual(type(n.place), str)

    def test_user(self):
        """test user """
        n = self.value()
        self.assertEqual(type(n.user), str)

    def test_text(self):
        """test the text """
        n = self.value()
        self.assertEqual(type(n.text), str)
