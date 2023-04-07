import sys

n, k = map(int, sys.stdin.readline().split())

list = list(map(int, sys.stdin.readline().split()))

list.sort(reverse=True)

print(list[k - 1])
