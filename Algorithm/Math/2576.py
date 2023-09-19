import sys

result = 0
mn = 100

for _ in range(7):
    a = int(sys.stdin.readline().rstrip())
    if a % 2 == 1:
        result += a
        mn = min(mn, a)
    else:
        continue

if result == 0:
    print(-1)
else:
    print(result)
    print(mn)
