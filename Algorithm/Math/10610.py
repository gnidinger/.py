import sys

n = sys.stdin.readline().strip()

total = sum(map(int, n))

if "0" in n and total % 3 == 0:
    result = "".join(sorted(n, reverse=True))
    print(result)
else:
    print(-1)
