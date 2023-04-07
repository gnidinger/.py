import sys

n = int(sys.stdin.readline())

b = []

for _ in range(n):
    temp = list(map(int, list(sys.stdin.readline().strip().split())))
    b.append(temp)

b.sort()

for i in b:
    print(*i)
