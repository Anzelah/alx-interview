#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """Function to calculate island perimeter"""
    per = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
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
