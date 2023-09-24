import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append((i, j))
        elif board[i][j] == 1:
            house.append((i, j))

chicken_combination = list(combinations(chicken, M))

min_distance = float("inf")

for i in chicken_combination:
    total_distance = 0

    for house_x, house_y in house:
        distance = min(
            abs(house_x - chicken_x) + abs(house_y - chicken_y) for chicken_x, chicken_y in i
        )
        total_distance += distance

    min_distance = min(min_distance, total_distance)

print(min_distance)
