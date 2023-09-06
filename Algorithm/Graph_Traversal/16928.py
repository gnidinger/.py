import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

board = [0] * 101
visited = [False] * 101

for _ in range(n + m):
    a, b = map(int, input().rstrip().split())
    board[a] = b

queue = deque()

queue.append([1, 0])
visited[1] = True

while queue:
    cur = queue.popleft()
    pos = cur[0]
    cnt = cur[1]

    if pos == 100:
        print(cnt)
        quit()

    for i in range(7):
        nextPos = pos + i

        if nextPos > 100:
            continue

        if board[nextPos] != 0:
            nextPos = board[nextPos]

        if not visited[nextPos]:
            visited[nextPos] = True
            queue.append([nextPos, cnt + 1])
