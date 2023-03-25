#!/usr/bin/python3
""" Module for testing amenity """
import unittest

class test_Console(unittest.TestCase):
    """ Class to test the Console method """

    def __init__(self, *args, **kwargs):
        """ Define __init__ function """
        super().__init__(*args, **kwargs)
        self.name = "Console"
