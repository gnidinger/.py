import sys

lines = sys.stdin.readlines()
board = [list(map(int, line.rstrip().split())) for line in lines]


def is_possible(row, col, num):
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    if (
        num in board[row]
        or num in [board[i][col] for i in range(9)]
        or num in [board[row_start + (i // 3)][col_start + (i % 3)] for i in range(9)]
    ):
        return False
    return True


def sudoku(row, col):
    if col == 9:
        return sudoku(row + 1, 0)

    if row == 9:
        return True

    if board[row][col] == 0:
        for num in range(1, 10):
            if is_possible(row, col, num):
                board[row][col] = num
                if sudoku(row, col + 1):
                    return True
                board[row][col] = 0
        return False
    else:
        return sudoku(row, col + 1)


lines = sys.stdin.readlines()
board = [list(map(int, line.rstrip().split())) for line in lines]

sudoku(0, 0)

for row in board:
    print(*row)
