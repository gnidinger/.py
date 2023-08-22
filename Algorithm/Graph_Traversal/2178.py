import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
map = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        current = queue.popleft()
        curX = current[0]
        curY = current[1]

        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]

            if (
                0 <= nx
                and nx < n
                and 0 <= ny
                and ny < m
                and map[nx][ny] == 1
                and not visited[nx][ny]
            ):
                queue.append([nx, ny])
                visited[nx][ny] = True
                map[nx][ny] = map[curX][curY] + 1


bfs(0, 0)

print(map[n - 1][m - 1])
