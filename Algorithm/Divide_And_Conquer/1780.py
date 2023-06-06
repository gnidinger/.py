import sys

n = int(sys.stdin.readline().rstrip())
paper = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]
count = [0] * 3


def is_same(row, col, size):
    color = paper[row][col]
    for i in range(row, row + size):
        for j in range(col, col + size):
            if paper[i][j] != color:
                return False
    return True


def divide(row, col, size):
    if is_same(row, col, size):
        count[paper[row][col] + 1] += 1
        return

    new_size = size // 3

    for i in range(3):
        for j in range(3):
            divide(row + new_size * i, col + new_size * j, new_size)


divide(0, 0, n)

print(*count, sep='\n')
