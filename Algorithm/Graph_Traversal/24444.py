from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().rstrip().split(" "))
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
order = [0] * (n + 1)
cnt = 1


def bfs(node):
    global cnt
    queue = deque()
    visited[node] = True
    order[node] = cnt
    cnt += 1
    queue.append(node)

    while queue:
        current = queue.popleft()
        for next in sorted(graph[current]):
            if not visited[next]:
                visited[next] = True
                order[next] = cnt
                cnt += 1
                queue.append(next)


for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split(" "))

    graph[u].append(v)
    graph[v].append(u)

bfs(r)

for i in range(1, n + 1):
    print(order[i])
