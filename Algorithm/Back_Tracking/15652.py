import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

lst = [0 for _ in range(m)]


def dfs(depth, start):
    if depth == m:
        for num in lst:
            print(num, '', end='')
        print()
        return

    for i in range(start, n + 1):
        lst[depth] = i
        dfs(depth + 1, i)


dfs(0, 1)
