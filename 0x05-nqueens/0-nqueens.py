#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """Check if placing a queen at (row, col) is safe."""
    for i in range(row):
        if (board[i] == col or
            board[i] - i == col - row or
            board[i] + i == col + row):
            return False
    return True


def solve_nqueens(n):
    """Solve the N Queens problem and print all solutions."""
    def solve(row, board):
        if row == n:
            print([[i, board[i]] for i in range(n)])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                solve(row + 1, board)

    board = [-1] * n
    solve(0, board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)

