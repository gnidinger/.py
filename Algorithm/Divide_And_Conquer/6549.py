import sys


def calc_max(height):
    n = len(height)
    max_area = 0

    for i in range(n):
        min_height = height[i]

        for j in range(i, n):
            min_height = min(min_height, height[j])
            temp = min_height * (j - i + 1)
            max_area = max(max_area, temp)

    return max_area


while True:
    n, *height = map(int, sys.stdin.readline().rstrip().split())

    if n == 0:
        break

    max_area = calc_max(height)

    print(max_area)
