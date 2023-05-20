#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data(list): A data set with values to be tested
    Returns:
        True if data is a valid UTF-8 encoding, else return False
    """
    if type(data) is not list:
        return None
    valid = True
    for value in data:
        if (type(value) is not int) or (not (0 <= value <= 127)):
            valid = False
            break

    return valid
