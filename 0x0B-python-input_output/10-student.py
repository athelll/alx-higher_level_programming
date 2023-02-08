#!/usr/bin/python3
"""

Class: Student
Function:

    def __init__(self, first_name, last_name, age)

    def to_json(self):
    returns: dictionary rep. of class

"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initialization Function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json but better"""
        if attrs is not None:
            dic = {}
            for keys in attrs:
                if keys in self.__dict__.keys():
                    dic[keys] = self.__dict__[keys]
            return dic
        else:
            return self.__dict__
