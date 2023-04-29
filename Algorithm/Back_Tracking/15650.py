import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

lst = [0 for _ in range(m)]
isVisited = [False] * (n + 1)


def dfs(start, depth):
    if depth == m:
        for num in lst:
            print(num, '', end='')
        print()
        return

    for i in range(start, n + 1):
        if isVisited[i] is False:
            isVisited[i] = True
            lst[depth] = i
            dfs(i, depth + 1)
            isVisited[i] = False


dfs(1, 0)
