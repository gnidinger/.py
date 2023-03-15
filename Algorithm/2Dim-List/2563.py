import sys

area = [0 for i in range(10000)]

n = int(sys.stdin.readline())

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    z = 100 * y + x
    for j in range(z, z + 1000, 100):
        for k in range(10):
            area[j + k] = 1

print(area.count(1))
