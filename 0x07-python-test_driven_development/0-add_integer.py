#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(j, k=98):
    """Adds two integers.

    Args:
        j: the first integer.
        k: the second integer, default 98.

    Raises:
        TypeError: if j, k are not int, float.

    Returns:
        The sum of the two integers.
    """

    if type(j) not in (int, float):
        raise TypeError('j must be an integer')
    if type(k) not in (int, float):
        raise TypeError('k must be an integer')
    return int(j) + int(k)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
