#!/usr/bin/python3
"""
a function that returns the perimeter
of the island described in grid
"""


def island_perimeter(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                # Each land cell contributes 4 sides initially

                # Check adjacent cells and deduct the shared sides
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Deduct 2 sides for adjacent land cells
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Deduct 2 sides for adjacent land cells

    return perimeter
