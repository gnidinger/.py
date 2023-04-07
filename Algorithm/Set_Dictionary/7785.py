import sys

n = int(sys.stdin.readline())
l = set()

for _ in range(n):
    a, b = sys.stdin.readline().strip().split()
    if b == 'enter':
        l.add(a)
    else:
        l.remove(a)

result = sorted(l, reverse=True)

print(*result, sep='\n')
