#!/usr/bin/python3
"""Solves the N queens puzzle using backtracking."""
import sys


def is_safe(queens, row, col):
    """Check if placing a queen at (row, col) is safe.

    Args:
        queens (list): List of column indices for already-placed queens,
            where the index in the list is the row.
        row (int): The row of the queen to place.
        col (int): The column of the queen to place.

    Returns:
        bool: True if no previously placed queen attacks this position.
    """
    for r in range(row):
        c = queens[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(n, row, queens, solutions):
    """Recursively try to place queens row by row (backtracking).

    Args:
        n (int): The size of the board.
        row (int): The current row being filled.
        queens (list): Column index chosen for each row so far.
        solutions (list): Accumulator for all valid solutions found.
    """
    if row == n:
        solutions.append([[r, queens[r]] for r in range(n)])
        return
    for col in range(n):
        if is_safe(queens, row, col):
            queens[row] = col
            solve(n, row + 1, queens, solutions)
            queens[row] = -1


def main():
    """Parse arguments, validate them, and print every solution."""
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

    solutions = []
    solve(n, 0, [-1] * n, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
