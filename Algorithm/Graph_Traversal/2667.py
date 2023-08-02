import sys

n = int(sys.stdin.readline().rstrip())
map = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
house = 0
houselst = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global house
    visited[x][y] = True
    house += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if map[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and not visited[i][j]:
            house = 0
            dfs(i, j)
            houselst.append(house)

houselst = sorted(houselst)

print(len(houselst))

for count in houselst:
    print(count)
