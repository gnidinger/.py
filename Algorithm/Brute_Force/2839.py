import sys

n = int(sys.stdin.readline())

cnt = 0

while True:
    if n < 0:
        print(-1)
        break
    if n % 5 == 0:
        print(n // 5 + cnt)
        break
    n = n - 3
    cnt += 1
