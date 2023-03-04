import sys

a = sys.stdin.readline().strip()

b = 1

for i in range(len(a) // 2):
    if a[i] != a[-(i + 1)]:
        b = 0

print(b)
