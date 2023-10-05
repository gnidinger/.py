import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())

    dp = [(0, 0)] * (N + 1)
    dp[0] = (1, 0)
    if N >= 1:
        dp[1] = (0, 1)

    for i in range(2, N + 1):
        dp[i] = (dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1])

    print(dp[N][0], dp[N][1])
