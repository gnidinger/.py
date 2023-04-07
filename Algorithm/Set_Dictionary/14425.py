import sys

n, m = map(int, sys.stdin.readline().split())

a = {sys.stdin.readline() for _ in range(n)}

cnt = 0

for i in range(m):
    if sys.stdin.readline() in a:
        cnt += 1

print(cnt)
