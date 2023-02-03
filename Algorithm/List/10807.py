import sys

n = int(sys.stdin.readline())

list = sys.stdin.readline().split()

v = sys.stdin.readline().rstrip()

count = 0

for i in list:
    if i == v:
        count += 1

print(count)