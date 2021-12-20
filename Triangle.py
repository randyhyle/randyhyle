#  File: Triangle.py
#  Description: Different algorithms implemented for the greatest
#  path sum.
#  Student Name: Randy Le
#  Student UT EID: hhl385
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 10/7/2021
#  Date Last Modified:

import sys

from timeit import timeit


# Returns the adjacent indices given the row and column
def get_adjacent_indices(row, column):
    return (row + 1, column), (row + 1, column + 1)


# recursive helper function for brute force
def recurse_brute(grid, row, column, current_sum, max_values):
    # Append to max values when we've reached the end and return
    # the current sum
    if row == len(grid) - 1:
        max_values.append(current_sum)
        return current_sum
    (r1, c1), (r2, c2) = get_adjacent_indices(row, column)
    left_sum = recurse_brute(grid, r1, c1, current_sum +
                             grid[r1][c1], max_values)
    right_sum = recurse_brute(grid, r2, c2, current_sum +
                              grid[r2][c2], max_values)
    return max(left_sum, right_sum)


# returns the greatest path sum using exhaustive search
def brute_force(grid):
    max_values = []
    recurse_brute(grid, 0, 0, grid[0][0], max_values)
    return max(max_values)


# returns the greatest path sum using greedy approach
def greedy(grid):
    # Set the base row and column to zero since that is where we are
    # starting
    current_row, current_col = 0, 0
    current_sum = grid[current_row][current_col]
    # Keep going until we reach the end of the length of the grid
    while current_row != len(grid) - 1:
        (r1, c1), (r2, c2) = get_adjacent_indices(current_row, current_col)
        left = grid[r1][c1]
        right = grid[r2][c2]
        if left > right:
            current_row, current_col = r1, c1
        else:
            current_row, current_col = r2, c2
        current_sum += grid[current_row][current_col]
    return current_sum


# Recursive helper function for divide and conquer
def recurse_divide_conquer(grid, row, column, current_sum):
    # Base case to stop when we reach the end of the row
    if row == len(grid) - 1:
        return current_sum
    (r1, c1), (r2, c2) = get_adjacent_indices(row, column)
    return max(recurse_divide_conquer(grid, r1, c1,
                                      current_sum + grid[r1][c1]),
               recurse_divide_conquer(grid, r2, c2,
                                      current_sum + grid[r2][c2]))


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
    return recurse_divide_conquer(grid, 0, 0, grid[0][0])


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    # start from the second to last row
    for r in reversed(range(len(grid)-1)):
        for c in range(r+1):  # go from first to last element in row
            (r1, c1), (r2, c2) = get_adjacent_indices(r, c)
            grid[r][c] += max(grid[r1][c1], grid[r2][c2])
    return grid[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]

    # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid


def main():
    # read triangular grid from file
    grid = read_file()

    # check that the grid was read in properly
    for row in grid:
        print(row)

    # output greatest path from exhaustive search
    times = timeit('brute_force({})'.format(grid),
                   'from __main__ import brute_force', number=10)
    times = times / 10
    # print time taken using exhaustive search
    print(times)

    # output greatest path from greedy approach
    times = timeit('greedy({})'.format(grid), 'from __main__ import greedy',
                   number=10)
    times = times / 10
    # print time taken using greedy approach
    print(times)

    # output greatest path from divide-and-conquer approach
    times = timeit('divide_conquer({})'.format(grid),
                   'from __main__ import divide_conquer', number=10)
    times = times / 10
    # print time taken using divide-and-conquer approach
    print(times)

    # output greatest path from dynamic programming
    times = timeit('dynamic_prog({})'.format(grid),
                   'from __main__ import dynamic_prog', number=10)
    times = times / 10
    # print time taken using dynamic programming
    print(times)


if __name__ == "__main__":
    main()
