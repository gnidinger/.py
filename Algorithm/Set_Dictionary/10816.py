import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
a = dict()

for i in x:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1

m = int(sys.stdin.readline())
y = list(map(int, sys.stdin.readline().split()))

for i in y:
    if i in a:
        print(a[i], end=' ')
    else:
        print(0, end=' ')
print()
