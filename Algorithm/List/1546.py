import sys

a = int(sys.stdin.readline())

b = list(map(int, sys.stdin.readline().split()))

c = [(i * 100) / max(b) for i in b]

print(sum(c) / a)
