#  File: Chess.py
#  Description: Program that counts the number of solutions given a
#  number of queens
#  Student Name: Hoang Randy Hy Le
#  Student UT EID: hhl385
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 10/17/2021
#  Date Last Modified:

import sys


class Queens(object):
    def __init__(self, n=8):
        self.n = n
        self.board = [['*' for _ in range(n)] for _ in range(n)]

    # print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()
        print()

    # check if a position on the board is valid
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # do the recursive backtracking
    def recursive_solve(self, col):
        if col == self.n:
            return 1
        else:
            count = 0
            for i in range(self.n):
                if self.is_valid(i, col):
                    self.board[i][col] = 'Q'
                    count += self.recursive_solve(col + 1)
                    self.board[i][col] = '*'
            return count

    # return the number of solutions present for a board
    def solve(self):
        return self.recursive_solve(0)


def main():
    # read the size of the board
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create a chess board
    game = Queens(n)
    print(game.solve())


if __name__ == "__main__":
    main()
