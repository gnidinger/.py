import sys

n = int(sys.stdin.readline().rstrip())
wire = [[0, 0]] * n
memo = [1 for _ in range(n)]

for i in range(n):
    wire[i] = list(map(int, sys.stdin.readline().rstrip().split()))

wire = sorted(wire)

for i in range(n):
    for j in range(i):
        if wire[j][1] < wire[i][1]:
            memo[i] = max(memo[i], memo[j] + 1)

mx = max(memo)

print(n - mx)
