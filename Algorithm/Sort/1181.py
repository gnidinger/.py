import sys

n = int(sys.stdin.readline())

a = set()

for _ in range(n):
    a.add(sys.stdin.readline().strip())

b = list(a)

c = sorted(b, key=lambda x: (len(x), x))

print(*c, sep='\n')
