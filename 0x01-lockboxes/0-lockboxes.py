#!/usr/bin/python3

"""
A function that checks if all boxes passed to it can be opened
"""


def canUnlockAll(boxes):
    """
    Checks if all boxes can be opened.

    Args:
        boxes (list): A list of lists, where each
        inner list represents the keys in a box.

    Returns:
        True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
