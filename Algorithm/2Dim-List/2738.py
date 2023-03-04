import sys

n, m = map(int, sys.stdin.readline().split())

list1 = []
list2 = []

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    list1.append(a)

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    list2.append(a)

for i in range(n):
    x = [a + b for a, b in zip(list1[i], list2[i])]
    print(*x)
