import sys

t = int(sys.stdin.readline().rstrip())

while t > 0:
    k = int(sys.stdin.readline().rstrip())
    files = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    dp = [[0 for _ in range(k + 1)] for _ in range(k + 1)]
    s = [0 for _ in range(k + 1)]

    for i in range(1, k + 1):
        s[i] = s[i - 1] + files[i]

    for i in range(2, k + 1):
        for j in range(1, k - i + 2):
            m = i + j - 1

            dp[j][m] = float("inf")

            for x in range(j, m):
                cost = dp[j][x] + dp[x + 1][m] + s[m] - s[j - 1]
                dp[j][m] = min(dp[j][m], cost)

    print(dp[1][k])

    t -= 1
