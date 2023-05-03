import sys

n = int(sys.stdin.readline().rstrip())
mod = 1_000_000_000
result = 0
memo = [[0 for _ in range(10)] for _ in range(n + 1)]

for i in range(1, 10):
    memo[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            memo[i][0] = memo[i - 1][1] % mod

        elif j == 9:
            memo[i][9] = memo[i - 1][8] % mod

        else:
            memo[i][j] = (memo[i - 1][j - 1] + memo[i - 1][j + 1]) % mod

result = sum(memo[n]) % mod

print(result)
