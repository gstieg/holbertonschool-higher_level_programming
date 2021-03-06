#!/usr/bin/python3
import json
import os


class Base:
    """ base class for modules"""

    __nb_objects = 0

    def __init__(self, id=None):
        """args:
        id: identification for the input"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ args:
        list_dictionaries - include all objects
        """
        if list_dictionaries == None or not list_dictionaries:
            return "[]"
        return (json.dumps(list_dictionaries))
