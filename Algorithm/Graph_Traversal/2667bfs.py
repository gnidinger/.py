import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
map = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    cnt = 1

    while queue:
        current = queue.popleft()

        for i in range(4):
            nx = current[0] + dx[i]
            ny = current[1] + dy[i]

            if (
                0 <= nx
                and nx < n
                and 0 <= ny
                and ny < n
                and map[nx][ny] == 1
                and not visited[nx][ny]
            ):
                queue.append([nx, ny])
                visited[nx][ny] = True
                cnt += 1

    return cnt


house_list = []

for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and not visited[i][j]:
            house_list.append(bfs(i, j))

house_list = sorted(house_list)

print(len(house_list))

for house in house_list:
    print(house)
