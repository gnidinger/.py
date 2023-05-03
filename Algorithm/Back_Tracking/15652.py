import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = [0 for _ in range(m)]


def dfs(start, depth):
    if depth == m:
        for num in lst:
            print(num, '', end='')
        print()
        return

    for i in range(start, n + 1):
        lst[depth] = i
        dfs(i, depth + 1)


dfs(1, 0)
