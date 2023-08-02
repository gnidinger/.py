from collections import deque
import sys

sys.setrecursionlimit(10**6)

n, m, v = map(int, sys.stdin.readline().rstrip().split(" "))
graph = [[] for _ in range(n + 1)]


def dfs(node, visited):
    visited[node] = True
    print(str(node), end=" ")
    for i in sorted(graph[node]):
        if not visited[i]:
            dfs(i, visited)


def bfs(node, visited):
    queue = deque()
    queue.append(node)
    visited[node] = True
    while queue:
        v = queue.popleft()
        print(str(v), end=" ")
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True


for i in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))

    graph[x].append(y)
    graph[y].append(x)

dfs_result = []
visited = [False] * (n + 1)
dfs(v, visited)
print(" ".join(dfs_result))

bfs_result = []
visited = [False] * (n + 1)
bfs(v, visited)
print(" ".join(bfs_result))
