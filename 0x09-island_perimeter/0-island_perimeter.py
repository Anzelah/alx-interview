#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """Function to calculate island perimeter"""

    length = len(grid[0])
    width = len(grid)

    land_cell = 0
    shared_edge = 0

    for r in range(width):
        for c in range(length):
            if (grid[r][c] == 1):
                land_cell += 1
                if (c > 0 and grid[r][c - 1] == 1):
                    shared_edge += 1
                if (r > 0 and grid[r - 1][c] == 1):
                    shared_edge += 1

    return (land_cell * 4) - (shared_edge * 2)
