import sys

sys.setrecursionlimit(10**6)

n, m, r = map(int, sys.stdin.readline().rstrip().split(" "))
graph = [[] for _ in range(n + 2)]
visited = [False] * (n + 1)
order = [0] * (n + 1)
cnt = 1


def dfs(node):
    global cnt

    visited[node] = True
    order[node] = cnt
    cnt += 1

    for next in sorted(graph[node], reverse=True):
        if not visited[next]:
            dfs(next)


for i in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[u].append(v)
    graph[v].append(u)

dfs(r)

for i in range(1, n + 1):
    print(order[i])
