import sys

n = int(sys.stdin.readline().rstrip())
result = 0
column = [0 for _ in range(n)]


def isPossible(depth):
    for i in range(depth):
        if column[i] == column[depth] or abs(column[depth] - column[i]) == depth - i:
            return False
    return True


def dfs(depth):
    global result

    if depth == n:
        result += 1
        return

    for i in range(n):
        column[depth] = i
        if isPossible(depth):
            dfs(depth + 1)


dfs(0)

print(result)
