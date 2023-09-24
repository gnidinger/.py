import sys
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def spread_virus(lab, virus):
    visited = set()
    for x, y in virus:
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            visited.add((cx, cy))
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                    if lab[nx][ny] == 0:
                        lab[nx][ny] = 2
                        stack.append((nx, ny))


N, M = map(int, sys.stdin.readline().rstrip().split())
lab = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

empty = []
virus = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

max_safe = 0

for walls in combinations(empty, 3):
    temp_lab = [row[:] for row in lab]
    for wx, wy in walls:
        temp_lab[wx][wy] = 1

    spread_virus(temp_lab, virus)

    safe = sum(row.count(0) for row in temp_lab)
    max_safe = max(max_safe, safe)

print(max_safe)
