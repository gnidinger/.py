import sys

n = int(sys.stdin.readline())

a = []

for x in range(n):
    i, j = sys.stdin.readline().strip().split()
    b = [int(x), int(i), j]
    a.append(b)

c = sorted(a, key=lambda x: (x[1], x[0]))


for i in c:
    print(i[1], i[2])
