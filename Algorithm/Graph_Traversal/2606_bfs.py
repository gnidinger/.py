import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0


def bfs(start):
    global cnt
    queue = deque()
    queue.append(start)
    visited[start] = True
    cnt += 1

    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                cnt += 1


for i in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(1)

print(cnt - 1)
