#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """Function to calculate island perimeter"""
    length = len(grid[0])
    width = len(grid)

    per = 0

    for r in range(width):
        for c in range(length):
            if (grid[r][c] == 1):
                if (grid[r][c - 1] == 0):
                    per += 1
                if (grid[r][c + 1] == 0):
                    per += 1
                if (grid[r - 1][c] == 0):
                    per += 1
                if (grid[r + 1][c] == 0):
                    per += 1

    return per
