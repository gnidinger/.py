import sys

n = int(sys.stdin.readline())
listx = []
listy = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    listx.append(x)
    listy.append(y)

a = max(listx) - min(listx)
b = max(listy) - min(listy)

print(a * b)
