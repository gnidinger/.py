import sys

n = int(sys.stdin.readline())

a = set(sys.stdin.readline().strip().split())

m = int(sys.stdin.readline())

b = list(sys.stdin.readline().strip().split())

for i in b:
    if i in a:
        print(1, end=' ')
    else:
        print(0, end=' ')

print()
