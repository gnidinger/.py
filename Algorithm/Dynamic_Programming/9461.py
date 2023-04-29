import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    m = int(sys.stdin.readline().rstrip())
    memo = [0 for _ in range(m + 1)]

    if m == 1:
        print(1)
        continue

    memo[0] = 0
    memo[1] = 1
    memo[2] = 1

    for i in range(3, m + 1):
        memo[i] = memo[i - 2] + memo[i - 3]

    print(memo[m])
