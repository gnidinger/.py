import sys

n = int(sys.stdin.readline())

b = []

for _ in range(n):
    temp = list(map(int, list(sys.stdin.readline().strip().split())))
    b.append(temp)

c = sorted(b, key=lambda x: (x[1], x[0]))

for i in c:
    print(*i)
