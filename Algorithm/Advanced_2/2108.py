import sys
import statistics

n = int(sys.stdin.readline().rstrip())

a = []
b = dict()

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    a.append(x)
    if x in b:
        b[x] += 1
    else:
        b[x] = 1

c = sorted([k for k, v in b.items() if max(b.values()) == v])

mode = c[0]

if len(c) > 1:
    mode = c[1]

print(round(statistics.mean(a)))
print(statistics.median(a))
print(mode)
print(max(a) - min(a))
