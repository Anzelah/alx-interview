#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """Function to calculate island perimeter"""
    
    length = len(grid[0])
    width = len(grid)

    per = 0
    e = 0

    for r in range(width):
        for c in range(length):
            if (grid[r][c] == 1):
                per += 1
                if (c > 0 and grid[r][c - 1] == 1):
                    e += 1
                if (r > 0 and grid[r - 1][c] == 1):
                    e += 1
                #if (grid[r - 1][c] == 0):
                #    per += 1
                #if (grid[r + 1][c] == 0):
                 #   per += 1

    return per * 4 - e * 2
