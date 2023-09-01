#!/usr/bin/python3
""" 5 island perimeter """


def island_perimeter(grid):
    """ find the perimeter of an island """
    i = 0
    per = 0
    height = len(grid)
    width = len(grid[0])

    while i < height:
        j = 0
        while j < width:
            if (j == 0 or j-1 >= 0) and grid[i][j] == 1:
                if j == 0:
                    per += 1
                elif grid[i][j-1] == 0:
                    per += 1

            if (i == 0 or i-1 >= 0) and grid[i][j] == 1:
                if i == 0:
                    per += 1
                elif grid[i-1][j] == 0:
                    per += 1

            if (j == width - 1 or j+1 < width) and grid[i][j] == 1:
                if j == width - 1:
                    per += 1
                elif grid[i][j+1] == 0:
                    per += 1

            if (i == height - 1 or i+1 < height) and grid[i][j] == 1:
                if i == height - 1:
                    per += 1
                elif grid[i+1][j] == 0:
                    per += 1
            j += 1
        i += 1
    return per
