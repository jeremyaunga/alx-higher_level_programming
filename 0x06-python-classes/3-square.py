#!/usr/bin/python3
"""Defines a class Square with a private attribute size and a public method area."""


class Square:
    """Class Square with a private attribute size and a public method area."""
    
    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

