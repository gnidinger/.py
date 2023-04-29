import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = [0] * m
isVisited = [False] * (n + 1)


def dfs(depth):
    if depth == m:
        for num in arr:
            print(num, '', end='')
        print()
        return

    for i in range(1, n + 1):
        if isVisited[i] is False:
            isVisited[i] = True
            arr[depth] = i
            dfs(depth + 1)
            isVisited[i] = False


dfs(0)
