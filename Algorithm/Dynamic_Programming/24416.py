import sys

recursion_cnt = 0
dp_cnt = 0

n = int(sys.stdin.readline().rstrip())
memo = [0 for _ in range(n + 1)]


def recursion(n):
    global recursion_cnt
    if n == 1 or n == 2:
        recursion_cnt += 1
        return 1
    else:
        return recursion(n - 1) + recursion(n - 2)


def dp(n):
    global dp_cnt
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n + 1):
        dp_cnt += 1
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


recursion(n)
dp(n)

print(recursion_cnt, dp_cnt)
