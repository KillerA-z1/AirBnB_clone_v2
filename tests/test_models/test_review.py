#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Test case class for testing the Review class."""

    def setUp(self):
        self.review = Review()

    def test_place_id(self):
        """Test the place_id attribute of the Review class."""
        self.assertEqual("", self.review.place_id)

    def test_user_id(self):
        """Test the user_id attribute of the Review"""
        self.assertEqual("", self.review.user_id)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test the text attribute of the Review class."""
        self.assertEqual("", self.review.text)

    def tearDown(self):
        """Clean up after each test."""
        pass


if __name__ == '__main__':
    unittest.main()
