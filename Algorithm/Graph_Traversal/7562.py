import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(l, start_x, start_y, end_x, end_y):
    visited = [[False] * l for _ in range(l)]
    queue = deque()
    queue.append([start_x, start_y, 0])
    visited[start_x][start_y] = True

    while queue:
        current = queue.popleft()
        x = current[0]
        y = current[1]
        cnt = current[2]

        if x == end_x and y == end_y:
            return cnt

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx and nx < l and 0 <= ny and ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny, cnt + 1])

    return -1


for i in range(t):
    l = int(sys.stdin.readline().rstrip())

    start_x, start_y = map(int, sys.stdin.readline().rstrip().split())
    end_x, end_y = map(int, sys.stdin.readline().rstrip().split())

    print(bfs(l, start_x, start_y, end_x, end_y))
