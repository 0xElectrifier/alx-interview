#!/usr/bin/python3
"""
Alx Interview: UTF-8 Validation
"""

from typing import List


def validUTF8(data: List) -> List[int]:
    """
    Method that determines if a given data set represents
    a valid UTF-8 encoding.
    Args:
        data(list): A data set with values to be tested
    Returns:
        True if data is a valid UTF-8 encoding, else return False
    """
    if type(data) is not list:
        return None
    valid = True
    for value in data:
        if value < 0 or value > 127:
            valid = False
            break

    return valid
