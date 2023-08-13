import sys

sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline().rstrip())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < m and 0 <= ny and ny < n:
            if field[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)


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
                dfs(x, y)
                cnt += 1

    print(cnt)
