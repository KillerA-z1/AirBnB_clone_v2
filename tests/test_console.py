#!/usr/bin/python3
"""Unittest module for the console"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel

class TestHBNBCommand(unittest.TestCase):
	def setUp(self):
		self.console = HBNBCommand()

	def tearDown(self):
		storage._FileStorage__objects = {}

	@patch('sys.stdout', new_callable=StringIO)
	def test_create_with_parameters(self, mock_stdout):
		self.console.onecmd('create BaseModel name="Test_Model" number=123 float_val=1.23')
		obj_id = mock_stdout.getvalue().strip()
		
		self.assertTrue(obj_id)
		
		obj = storage.all()[f"BaseModel.{obj_id}"]
		self.assertEqual(obj.name, "Test Model")
		self.assertEqual(obj.number, 123)
		self.assertEqual(obj.float_val, 1.23)

	@patch('sys.stdout', new_callable=StringIO)
	def test_create_with_invalid_parameters(self, mock_stdout):
		self.console.onecmd('create BaseModel invalid_param name="Valid_Name"')
		obj_id = mock_stdout.getvalue().strip()
		
		self.assertTrue(obj_id)
		
		obj = storage.all()[f"BaseModel.{obj_id}"]
		self.assertEqual(obj.name, "Valid Name")
		self.assertFalse(hasattr(obj, 'invalid_param'))

	@patch('sys.stdout', new_callable=StringIO)
	def test_create_with_escaped_quotes(self, mock_stdout):
		self.console.onecmd('create BaseModel name="Test_\\"Quoted\\"_Name"')
		obj_id = mock_stdout.getvalue().strip()
		
		self.assertTrue(obj_id)
		
		obj = storage.all()[f"BaseModel.{obj_id}"]
		self.assertEqual(obj.name, 'Test "Quoted" Name')


if __name__ == "__main__":
    unittest.main()
