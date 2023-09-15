import sys

x = int(sys.stdin.readline().rstrip())
cnt = 0

while x > 0:
    cnt += x % 2
    x //= 2

print(cnt)
