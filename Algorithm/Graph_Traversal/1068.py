import sys

n = int(sys.stdin.readline().rstrip())
cnt = 0
tree = [[] for _ in range(n)]
visited = [False] * n
root = -1


def dfs(node):
    global cnt

    visited[node] = True

    if not tree[node]:
        cnt += 1
        return

    for child in tree[node]:
        if not visited[child]:
            dfs(child)


def remove_node(node):
    visited[node] = True

    for parent_node in tree:
        if node in parent_node:
            parent_node.remove(node)

    for child in tree[node]:
        if not visited[child]:
            remove_node(child)

    tree[node].clear()


parents = list(map(int, sys.stdin.readline().split(" ")))

for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        tree[parents[i]].append(i)

removeNode = int(sys.stdin.readline().rstrip())

if removeNode == root:
    print(0)
    sys.exit()

remove_node(removeNode)
dfs(root)
print(cnt)
