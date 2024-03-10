#!/usr/bin/python3
"""test state class """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """test for state"""

    def __init__(self, *args, **kwargs):
        """init arg and kwargs """
        super().__init__(*args, **kwargs)
        self.name = "egypt"
        self.value = egypt

    def test_name(self):
        """test case """
        n = self.value()
        self.assertEqual(type(n.name), str)
