#!/usr/bin/python3
'''
This module introduces a function.
'''
import sys


def is_safe(board, row, col, N):
    """
    Function to check if it is safe to place a queen in the given cell.

    board: The corrent state of the chess board.
    row: The row index of the cell being checked.
    col: The colu,mn ndex of the cell being checked.
    N: The size of the board(N * N).

    Return: True if is safe to place a queen, otherwise False
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(N):
    """
    Function to solve N-queen problems and print all possible
    solutions
    N: The size of the checcboard and number of queens.
    """
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]

    def solve_util(board, col):
        """
        Function for solving the N quuen problem using backtracking.

        board: The currnt state of the chess board
        col: The column index for placing the queen.

        Return True if solution is found, otherwise False.
        """
        if col >= N:
            solution = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        solution.append([i, j])
            print(solution)
            return True

        res = False
        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1

                # Recursive call to place queen in the next column
                res = solve_util(board, col + 1) or res

                # backtracking if placing a queen in the current column
                board[i][col] = 0
        return res
    solve_util(board, 0)


if __name__ == "__main__":
    # Validating and processing the input arguements
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(N)
