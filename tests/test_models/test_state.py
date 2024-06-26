#!/usr/bin/python3
"""Unittest module for the State Class."""

from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest


class test_state(test_basemodel):
    """Tests for the State class."""

    def test_state(self):
        """Test for the State class."""
        state = State()
        self.assertEqual(state.name, "")
        state.name = "California"
        self.assertEqual(state.name, "California")
        self.assertEqual(state.to_dict()["name"], "California")

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
