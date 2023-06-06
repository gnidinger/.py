import sys

n = int(sys.stdin.readline().rstrip())
white = 0
blue = 0
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]


def is_same(row, col, size):
    color = board[row][col]
    for i in range(row, row + size):
        for j in range(col, col + size):
            if board[i][j] != color:
                return False
    return True


def quadrant(row, col, size):
    global white, blue
    if is_same(row, col, size):
        if board[row][col] == 0:
            white += 1
            return
        else:
            blue += 1
            return

    new_size = size // 2

    quadrant(row, col, new_size)
    quadrant(row, col + new_size, new_size)
    quadrant(row + new_size, col, new_size)
    quadrant(row + new_size, col + new_size, new_size)


quadrant(0, 0, n)

print(white)
print(blue)
