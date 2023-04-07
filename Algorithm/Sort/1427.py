import sys

a = list(map(int, list(sys.stdin.readline().strip())))

a.sort(reverse=True)

print(*a, sep='')
