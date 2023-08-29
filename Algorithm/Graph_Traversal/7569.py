import sys
from collections import deque

input = sys.stdin.readline


class Tomato:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


m, n, h = map(int, input().split())
box = [[[0] * m for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

deque = deque()

for i in range(h):
    for j in range(n):
        row = list(map(int, input().split()))
        for k in range(m):
            box[i][j][k] = row[k]
            if box[i][j][k] == 1:
                deque.append(Tomato(k, j, i))
                visited[i][j][k] = True


def bfs(deque):
    days = 0
    while deque:
        size = len(deque)
        for _ in range(size):
            tomato = deque.popleft()
            for i in range(6):
                nx = tomato.x + dx[i]
                ny = tomato.y + dy[i]
                nz = tomato.z + dz[i]

                if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
                    continue

                if visited[nz][ny][nx] or box[nz][ny][nx] == -1:
                    continue

                visited[nz][ny][nx] = True
                box[nz][ny][nx] = 1
                deque.append(Tomato(nx, ny, nz))

        if deque:
            days += 1

    return days


days = bfs(deque)
if days < 0:
    days = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print(-1)
                quit()

print(days)
