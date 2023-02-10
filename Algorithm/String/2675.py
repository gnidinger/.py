import sys

t = int(sys.stdin.readline())

result = []

for i in range(t):
    a, b = sys.stdin.readline().split()
    c = list(b)
    d = ''
    for j in c:
        d += j * int(a)
    result.append(d)

print(*result, sep='\n')
