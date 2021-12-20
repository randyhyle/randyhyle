#  File: WordSearch.py
#  Description: A file that finds the words in a word search puzzle.
#  Student Name: Hoang Randy Hy Le
#  Student UT EID: hhl385
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 9/1/2021
#  Date Last Modified: 9/4/2021

import sys


def read_input():
    """ Input: None
    Output: function returns a 2-D list that is the grid of letters
    and 1-D list of words to search"""
    puzzle = []
    num_rows = int(sys.stdin.readline())
    # Assuming there are blank lines between the integers and the
    # puzzle, just read the blank line and do nothing with it.
    sys.stdin.readline()

    for i in range(num_rows):
        puzzle.append(sys.stdin.readline().rstrip().split(' '))
    sys.stdin.readline()

    word_bank = []
    num_words = int(sys.stdin.readline())
    for i in range(num_words):
        word_bank.append(sys.stdin.readline().rstrip())

    return puzzle, word_bank


def find_word(grid, word):
    """Input: a 2-D list representing the grid of letters and a single
            string representing the word to search
    Output: returns a tuple (i, j) containing the row number and the
            column number of the word that you are searching
            or (0, 0) if the word does not exist in the grid"""
    location = find_word_horizontal(grid, word)
    # If the function returns anything but none return location.
    # Otherwise, move on to the next function.
    if location:
        return location

    location = find_word_vertical(grid, word)
    if location:
        return location

    location = find_word_diagonal_backward(grid, word)
    if location:
        return location

    location = find_word_diagonal_forward(grid, word)
    if location:
        return location

    return 0, 0


def find_word_horizontal(grid, word):
    """Function to check if a word exists on the word puzzle in
    a horizontal manner. Will return a tuple containing the row number
    and the column number of the word that it is initially found.
    """
    size = len(grid)
    for row in range(size):
        # Set grid string to an empty string everytime the loop
        # iterates
        grid_string = ''
        for col in range(size):
            grid_string += grid[row][col]
        # Reading right to left
        if word in grid_string:
            found_word = (row + 1, grid_string.index(word) + 1)
            return found_word
        # Left to right
        elif word in grid_string[::-1]:
            found_word = (row + 1, size - grid_string[::-1].index(word))
            return found_word


def find_word_vertical(grid, word):
    """Function to check if a word exists on the word puzzle in
    a vertical manner."""
    for col in range(len(grid[0])):
        grid_string = ''
        for row in grid:
            grid_string += row[col]
        # Top to bottom
        if word in grid_string:
            found_word = (grid_string.index(word) + 1, col + 1)
            return found_word
        # Bottom to top
        elif word in grid_string[::-1]:
            found_word = (len(grid) - grid_string[::-1].index(word), col + 1)
            return found_word


def find_word_diagonal_backward(grid, word):
    """Function to check if a word exists on the word puzzle in a
    right to left diagonal manner."""
    size = len(grid)
    for i in range(size):
        inverse = size - i - 1
        found_word = build_diagonal_backward(grid, word, i, 0, inverse)
        if found_word:
            return found_word
        found_word = build_diagonal_backward(grid, word, i, i, size - 1)
        if found_word:
            return found_word


def build_diagonal_backward(grid, word, i, start_row, start_col):
    """Given the starting row and column, find the diagonals for the
    top or bottom half of the matrix going right to left,
    If the word is found in the diagonal, return the found words
    coordinates."""
    grid_string = ''

    # Build the string for each time we iterate through i
    for j in range(len(grid) - i):
        grid_string += grid[start_row + j][start_col - j]
    # Top to bottom
    if word in grid_string:
        j = grid_string.index(word)
        found_word = (start_row + j + 1, start_col - j + 1)
        return found_word
    # Bottom to top
    elif word in grid_string[::-1]:
        j = len(grid) - 1 - i - grid_string[::-1].index(word)
        found_word = (start_row + j + 1, start_col - j + 1)
        return found_word


def find_word_diagonal_forward(grid, word):
    """Function to check if a word exists on the word puzzle in a
    left to right diagonal manner."""
    for i in range(len(grid)):
        found_word = build_diagonal_forward(grid, word, i, 0, i)
        if found_word:
            return found_word
        found_word = build_diagonal_forward(grid, word, i, i, 0)
        if found_word:
            return found_word


def build_diagonal_forward(grid, word, i, start_row, start_col):
    """Given the starting row and column, find the diagonals for the
    top or bottom half of the matrix going left to right,
    If the word is found in the diagonal, return the found words
    coordinates."""
    grid_string = ''

    # Build the string for each time we iterate through i
    for j in range(len(grid) - i):
        grid_string += grid[start_row + j][start_col + j]
    # Top to bottom
    if word in grid_string:
        j = grid_string.index(word)
        found_word = (start_row + j + 1, start_col + j + 1)
        return found_word
    # Bottom to top
    elif word in grid_string[::-1]:
        j = len(grid) - i - grid_string[::-1].index(word)
        found_word = (start_row + j, start_col + j)
        return found_word


def main():
    """read the input file from stdin"""
    word_grid, word_list = read_input()

    # find each word and print its location
    for word in word_list:
        location = find_word(word_grid, word)
        print(word + ": " + str(location))


if __name__ == "__main__":
    main()
