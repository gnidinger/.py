import sys

N = int(sys.stdin.readline().rstrip())

T = []
P = []

dp = [0] * (N + 1)

for _ in range(N):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    T.append(t)
    P.append(p)

for i in range(N):
    dp[i + 1] = max(dp[i + 1], dp[i])
    if i + T[i] <= N:
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

print(max(dp))
