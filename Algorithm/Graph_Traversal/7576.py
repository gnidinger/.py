import sys
from collections import deque

queue = deque()
m, n = map(int, sys.stdin.readline().rstrip().split())
box = [list(map(int, list(sys.stdin.readline().rstrip().split(" ")))) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue):
    while queue:
        current = queue.popleft()
        for i in range(4):
            nx = current[0] + dx[i]
            ny = current[1] + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[current[0]][current[1]] + 1
                queue.append([nx, ny])


for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])

bfs(queue)

result = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            quit()
        result = max(result, box[i][j])

print(result - 1)
