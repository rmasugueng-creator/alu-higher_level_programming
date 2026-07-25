#!/usr/bin/python3
"""Defines MagicClass, reproducing a given bytecode disassembly."""
import math


class MagicClass:
    """Represents a circle-like shape defined by a radius."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass instance.

        Args:
            radius (int/float): The radius of the instance.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle defined by the radius."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle defined by the radius."""
        return 2 * math.pi * self.__radius
