import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0


def dfs(node):
    global cnt
    visited[node] = True
    cnt += 1

    for next in graph[node]:
        if not visited[next]:
            dfs(next)


for i in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[u].append(v)
    graph[v].append(u)

dfs(1)

print(cnt - 1)
