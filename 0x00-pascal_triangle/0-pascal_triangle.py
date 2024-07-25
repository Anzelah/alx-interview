#!/usr/bin/python3
"""Solving pascals triangle
"""


def pascal_triangle(n):
    """
    Return list of lists of integers representing the Pascal’s triangle of n.
    Returns: an empty list if n <= 0
    You can assume n will be always an integer
    """
    if n <= 0:
        return []
    #row_0 =       [1]
    #row_1 =      [1, 1]
    #row_3 =     [1, 2, 1]
    #row_4 =    [1, 3, 3, 1]
    #row_5 =   [1, 4, 6, 4, 1]
    #elements = nth row + 1
    #rows start at 0
    #all numbers at both ends wll always be 1
    #n is number of rows to be printed
    for i in range(1, n+1): # columns of each row
        print(i)
