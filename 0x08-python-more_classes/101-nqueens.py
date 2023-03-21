#!/usr/bin/python3


import sys

def nQueens(n):
    """
    The N queens puzzle is the challenge of placing N non-attacking 
    queens on an N×N chessboard. Write a program that solves the N queens problem.

    Usage: nqueens N
         If the user called the program with the wrong number of arguments,
         print Usage: nqueens N, followed by a new line, and exit with the status 1
         where N must be an integer greater or equal to 4
         If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
         If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
    The program should print every possible solution to the problem
    One solution per line
    Format: see example
    You don’t have to print the solutions in a specific order
    You are only allowed to import the sys module
    """
    queens = [0] * n
    print(queens)
    s = n

    while True:
        while(n > 1):
            if valid(queens, n) == True:
                n = n -1
            else:
                queens[n] += 1
                if queens[n] >= s:
                    queens[n] = 0
                    queens[n + 1] += 1
        print("solution")
        print[queens]
        queens[0] += 1
        n = 0

    def valid(queens, n):
        i = n + 1
        while i < s:
            if (queens[i] == queens[n]):
                return False
        i = n + 1
        while i < s:
            x = 1
            if queens[i] == (queens[n] - x):
                return False
            i + 1
            x + 1
        i = n +1
        while i < s:
            x = 1
            if queens[i] == (queens[n] + x):
                return False
            i + 1
            x + 1
        return True

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except (ValueError, TypeError):
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    nQueens(n)
