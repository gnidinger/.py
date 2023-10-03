import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in [1, 2, 3]:
            if i - j >= 0:
                dp[i] += dp[i - j]

    print(dp[n])
