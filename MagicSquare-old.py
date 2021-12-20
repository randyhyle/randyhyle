#  File: MagicSquare-old.py
#  Description: Given dimensions that are greater than 1 and odd,
#  return a square that has no duplicate numbers and all rows,
#  columns, and diagonals sum up to the same value.
#  Student's Name: Hoang Randy Hy Le
#  Student's UT EID: hhl385
#  Partner's Name:
#  Partner's UT EID:
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 9/7/2021
#  Date Last Modified:

import sys


# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def make_square(n):
    # create a grid with placeholder values according to n
    square_list = [[0 for _ in range(n)] for _ in range(n)]
    row = n - 1
    col = int(((n + 1) / 2) - 1)
    # populate the grid with unique values from 1 to n**2
    for i in range(1, (n ** 2) + 1):
        square_list[row][col] = i
        row += 1
        col += 1

        if row == n and col == n:
            row = n - 2
            col = n - 1
        elif row == n:
            row = 0
        elif col == n:
            col = 0
        if square_list[row][col] != 0:
            row -= 2
            col -= 1

    return square_list


# Print the magic square in a neat format where the numbers
# are right justified. This is a helper function.
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square(magic_square):
    dimension_size = len(magic_square)
    square = ''
    for row in range(dimension_size):
        grid_string = ''
        for col in range(dimension_size):
            grid_string += str(magic_square[row][col]) + ' '
        grid_string += '\b'
        square += grid_string + '\n'
    print(square.strip())


# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# This is a helper function.
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square(magic_square):
    n = len(magic_square)

    diagonal_sum1 = 0
    diagonal_sum2 = 0
    # traverse through grid diagonally one time each for left to right
    # and right to left
    for i in range(n):
        diagonal_sum1 += magic_square[i][i]
        diagonal_sum2 += magic_square[i][n - i - 1]

    # return false if diagonals don't match
    if diagonal_sum1 != diagonal_sum2:
        return False

    for i in range(n):
        row_sum = 0
        col_sum = 0
        for j in range(n):
            row_sum += magic_square[i][j]
            col_sum += magic_square[j][i]
        # add each row together, and each column together per loop
        # compare the sum of each row and col along with diag sum
        # return False if any do not match each other
        if not(row_sum == col_sum == diagonal_sum1):
            return False
    # if it is a magic square, return True
    return True


# Input: square is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the magic square
#         if n is outside the range return 0
def sum_adjacent_numbers(square, n):
    # if n is not in the grid, return 0
    if n > len(square) ** 2 or n <= 0:
        return 0

    row, col = get_index_n(square, n)

    adjacent_sum = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            # make sure we are adding the numbers adjacent to n and
            # negative indexes are not counted to account for edge
            # cases
            if len(square) > i >= 0 and len(square) > j >= 0:
                if square[i][j] != square[row][col]:
                    adjacent_sum += square[i][j]

    return adjacent_sum


def get_index_n(square, n):
    """Function that returns the coordinates in the square where n
    resides."""

    for row in range(len(square)):
        for col in range(len(square)):
            if n == square[row][col]:
                return row, col


def main():
    # read the input file from stdin
    num = int(sys.stdin.readline())
    # create the magic square
    magic_square = make_square(num)

    # print the sum of the adjacent numbers
    for n in sys.stdin.readlines():
        sum_of_num = sum_adjacent_numbers(magic_square, int(n))
        print(sum_of_num)


# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
