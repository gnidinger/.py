import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = [0 for _ in range(m)]
memo = [False for _ in range(n + 1)]


def dfs(depth):
    if depth == m:
        for i in lst:
            print(i, '', end='')
        print()
        return
    for i in range(1, n + 1):
        lst[depth] = i
        dfs(depth + 1)


dfs(0)
