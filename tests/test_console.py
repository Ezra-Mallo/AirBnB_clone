#!/usr/bin/python3
"""Module for TestHBNBCommand class."""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os


class TestHBNBCommand(unittest.TestCase):
    """
        Tests HBNBCommand console

    """

    def setUp(self):
        print("Testing Console methods")

    def test_help_quit(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        s = 'Quit command to exit the program\n        \n'
        self.assertEqual(s, f.getvalue())

    def test_help_create(self):
        """Tests the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        s = 'Creates a new instance of BaseModel\n        '\
            'saves it (to the JSON file) and prints the id'\
            '\n        \n'
        self.assertEqual(s, f.getvalue())

    """
    def test_help_clear(self):
        # Tests default
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help clear")
            s = 'Clear the screen\n'
            self.assertEqual(s, f.getvalue())
    """

    def test_help_show(self):
        # Tests show
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            s = 'Prints the string representation of an instance\n        '\
                'based on the class name and id'\
                '\n        \n'
            self.assertEqual(s, f.getvalue())

    def test_help_destroy(self):
        """Tests destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            s = 'Deletes an instance\n        '\
                'based on the class name and id\n        '\
                'and saves the change into the JSON file'\
                '\n        \n'
            self.assertEqual(s, f.getvalue())

    def test_help_all(self):
        """Tests All"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            s = 'Prints all string representation of all instances'\
                '\n        based or not on the class name\n        \n'
            self.assertEqual(s, f.getvalue())


if __name__ == "__main__":
    unittest.main()
