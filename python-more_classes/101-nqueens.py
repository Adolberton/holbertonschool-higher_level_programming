#!/usr/bin/python3
import sys

def is_valid_input(args):
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(args[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
        board[i] - i == col - row or \
        board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, n):
    if row == n:
        print_solution(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)

def print_solution(board, n):
    coordinates = [[i, board[i]] for i in range(n)]
    print(coordinates)

def main():
    n = is_valid_input(sys.argv)
    board = [-1] * n
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    main()
