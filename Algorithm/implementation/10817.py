import sys

lst = list(map(int, sys.stdin.readline().rstrip().split(" ")))

lst = sorted(lst)

print(lst[1])
