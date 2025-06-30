# You are given two coordinates (x1, y1) and (x2, y2) of a two-dimensional graph. Find the distance between them.

import math

def calculate_distance(x1, y1, x2, y2):
    """
    Calculate the distance between two points in a 2D space.

    Parameters:
    x1, y1 : float : coordinates of the first point
    x2, y2 : float : coordinates of the second point

    Returns:
    float : distance between the two points
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

x1, y1 = (3, 4)
x2, y2 = (7, 7)

print(calculate_distance(x1, y1, x2, y2))  # Output: 5.0