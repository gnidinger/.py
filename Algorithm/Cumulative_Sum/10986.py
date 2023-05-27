import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = [0] * m

for i in range(n):
    if i > 0:
        lst[i] = lst[i - 1] + lst[i]
    remain = lst[i] % m
    cnt[remain] += 1

result = cnt[0]

for i in range(m):
    result += (cnt[i] * (cnt[i] - 1)) // 2

print(result)
