import sys

n = int(sys.stdin.readline().rstrip())
video = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
result = ''


def is_same(row, col, size):
    color = video[row][col]
    for i in range(row, row + size):
        for j in range(col, col + size):
            if video[i][j] != color:
                return False
    return True


def quadrant(row, col, size):
    global result

    if is_same(row, col, size):
        result += str(video[row][col])
        return

    new_size = size // 2

    result += '('
    quadrant(row, col, new_size)
    quadrant(row, col + new_size, new_size)
    quadrant(row + new_size, col, new_size)
    quadrant(row + new_size, col + new_size, new_size)
    result += ')'


quadrant(0, 0, n)

print(result)
