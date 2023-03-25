#!/usr/bin/python3
""" Module for testing amenity """
from tests.test_models.test_base_model import test_basemodel
from models.console import Console

class test_Console(test_basemodel):
    """ Class to test the Console method """

    def __init__(self, *args, **kwargs):
        """ Define __init__ function """
        super().__init__(*args, **kwargs)
        self.name = "Console"
        self.value = Console
