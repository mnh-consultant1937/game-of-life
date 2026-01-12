# The state of the grid changes over time based on a few simple rules:

# Any live cell with fewer than 2 live neighbors dies (underpopulation).

# Any live cell with 2 or 3 live neighbors lives on.

# Any live cell with more than 3 live neighbors dies (overpopulation).

# Any dead cell with exactly 3 live neighbors becomes alive (reproduction)



# Before the game can “live”, we need two things:

# A way to mark a cell as alive

# A way to count its neighboring live cells


# Every cell has up to 8 neighbors


# Game of Life always works in two phases:

# Observe (count neighbors)

# Decide (live or die)


# grid = [[0 for _ in range(3)] for _ in range(2)]
# print(grid)

# for row in grid:
#     print(row)

# WIDTH = 4
# HEIGHT = 3

# grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
# print(grid)



# [expression for variable in iterable]
# expression → what each element of the list will be

# variable → takes each value from iterable

# iterable → something you can loop over (like range, list, string, etc.)

# squares = [x**2 for x in range(5)]
# print(squares)

# squares = []
# for x in range(5):
#     squares.append(x**2)

# print(squares)

# for i in range(3):
#   print(i)

# row = [i for i in range(3)]
# print(row)



# grid = [[0 for _ in range(3)] for _ in range(2)]
# print(grid)

# for row in grid:
#   print(row)



# neighbors = [(-1,-1), (-1,0), (-1,1),
#                  (0,-1),         (0,1),
#                  (1,-1), (1,0), (1,1)]

# for dr, dc in neighbors:
#   print(dr, dc)




