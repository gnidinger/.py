import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
memories = [0] + list(map(int, sys.stdin.readline().rstrip().split(" ")))
costs = [0] + list(map(int, sys.stdin.readline().rstrip().split(" ")))

sum_cost = sum(costs)
dp = [0] + [float("-inf") for _ in range(sum_cost)]

for i in range(1, n + 1):
    for j in range(sum_cost, costs[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - costs[i]] + memories[i])

result = 0

for i in range(sum_cost + 1):
    if dp[i] >= m:
        result = i
        break

print(result)
