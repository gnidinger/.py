import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        current = queue.pop()

        for i in range(4):
            nx = current[0] + dx[i]
            ny = current[1] + dy[i]

            if 0 <= nx and nx < m and 0 <= ny and ny < n:
                if field[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = True


for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    field = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        field[x][y] = 1

    cnt = 0

    for x in range(m):
        for y in range(n):
            if field[x][y] == 1 and not visited[x][y]:
                bfs(x, y)
                cnt += 1

    print(cnt)
