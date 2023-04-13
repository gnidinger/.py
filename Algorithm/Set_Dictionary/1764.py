import sys

n, m = map(int, sys.stdin.readline().split())

a = {sys.stdin.readline().strip() for _ in range(n)}
b = {sys.stdin.readline().strip() for _ in range(m)}

list = sorted(a.intersection(b))

print(len(list))
print(*list, sep='\n')
