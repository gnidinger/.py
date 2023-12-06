import sys

n = int(sys.stdin.readline().rstrip())
blocks = list(map(int, sys.stdin.readline().split()))

# dp 배열 초기화
dp = [float("inf")] * n
dp[0] = 0

# 동적 프로그래밍
for i in range(n):
    for j in range(1, blocks[i] + 1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[n - 1] == float("inf"):
    print(-1)
else:
    print(dp[n - 1])
