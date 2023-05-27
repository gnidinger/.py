import sys

lines = sys.stdin.readlines()
board = [list(map(int, line.rstrip().split())) for line in lines]


def is_possible(row, col, num):
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for i in range(9):
        if (
            board[row][i] == num
            or board[i][col] == num
            or board[row_start + (i // 3)][col_start + (i % 3)] == num
        ):
            return False
    return True


def sudoku(row, col):
    if col == 9:
        return sudoku(row + 1, 0)

    if row == 9:
        output = '\n'.join([' '.join(map(str, row)) for row in board])
        print(output)
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


sudoku(0, 0)
