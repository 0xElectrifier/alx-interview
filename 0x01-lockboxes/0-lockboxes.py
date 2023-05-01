#!/usr/bin/python3
"""A module that defines a method, `canUnlockAll`"""


def canUnlockAll(boxes):
    """Determines if all @boxes can be opened

    Args:
        boxes (list): a list of lists
    Returns: True if all boxes can be opended, else return False
    """
    box_length = len(boxes);
    found_keys = set();

    for box in boxes:
        for key in box:
            if (key > 0 and key < box_length):
                found_keys.add(key)

    return found_keys;
