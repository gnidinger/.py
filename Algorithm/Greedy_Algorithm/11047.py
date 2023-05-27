import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
cnt = 0

for i in range(n - 1, -1, -1):
    if k >= coins[i]:
        cnt += k // coins[i]
        k %= coins[i]

print(cnt)
