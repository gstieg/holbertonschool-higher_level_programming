#!/usr/bin/python3


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """
        args:
        first_name: first Name of the student
        last_name: last name of the student
        age: age the the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
