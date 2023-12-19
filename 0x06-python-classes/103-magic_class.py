#!/usr/bin/python3
"""Defines a class MagicClass that mimics a given Python bytecode."""

import math


class MagicClass:
    """Mimics a given Python bytecode."""

    def __init__(self, radius=0):
        """Initializes a new MagicClass instance.

        Args:
            radius (int): The radius of the MagicClass instance.
        """
        self.radius = radius

    @property
    def radius(self):
        """Retrieves the radius of the MagicClass instance."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Sets the radius of the MagicClass instance.

        Args:
            value (int): The new radius of the MagicClass instance.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("radius must be an integer")
        elif value < 0:
            raise ValueError("radius must be >= 0")
        self.__radius = value

    def area(self):
        """Computes the area of the MagicClass instance."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Computes the circumference of the MagicClass instance."""
        return 2 * math.pi * self.__radius

