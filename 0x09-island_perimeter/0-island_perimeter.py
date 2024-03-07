#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """Function to calculate island perimeter"""
    per = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (grid[r][c] == 1):
                if (c == 0 or grid[r][c - 1] == 0):
                    per += 1
                if (c == len(grid[0]) - 1 or grid[r][c + 1] == 0):
                    per += 1
                if (r == 0 or grid[r - 1][c] == 0):
                    per += 1
                if (r == len(grid[r]) - 1 or grid[r + 1][c] == 0):
                    per += 1

    return per
