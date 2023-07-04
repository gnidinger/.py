import sys

m, n = map(int, sys.stdin.readline().rstrip().split(" "))
map = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < m and ny < n:
            if map[nx][ny] < map[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]


print(dfs(0, 0))
