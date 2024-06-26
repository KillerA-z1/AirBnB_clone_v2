#!/usr/bin/python3
"""Unittest module for the City Class."""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class TestCity(unittest.TestCase):
    """Test case class for testing the City class."""

    def test_attributes(self):
        """Test the attributes of the City class."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
