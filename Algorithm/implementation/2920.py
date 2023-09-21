import sys

lst = list(map(int, sys.stdin.readline().rstrip().split()))

asc = sorted(lst)
des = sorted(lst, reverse=True)

if lst == asc:
    print("ascending")
elif lst == des:
    print("descending")
else:
    print("mixed")
