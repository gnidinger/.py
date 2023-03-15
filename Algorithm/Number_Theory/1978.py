import sys

n = int(sys.stdin.readline())

list = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in list:
    x = 0
    for j in range(1, i):
        if i % j == 0:
            x += 1
    if x == 1:
        cnt += 1

print(cnt)
