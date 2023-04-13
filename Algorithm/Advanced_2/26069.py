import sys

n = int(sys.stdin.readline().rstrip())

x = set()

for i in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    if a == 'ChongChong':
        x.add(a)
        x.add(b)
        continue
    elif b == 'ChongChong':
        x.add(a)
        x.add(b)
        continue
    elif a in x:
        x.add(b)
        continue
    elif b in x:
        x.add(a)
        continue

print(len(x))
