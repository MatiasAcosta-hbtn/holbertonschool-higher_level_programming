#!/usr/bin/python3
"""Module of geometry"""


class BaseGeometry:
    """Class about base geometry"""

    def area(self):
        """Calculate area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validator of integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
