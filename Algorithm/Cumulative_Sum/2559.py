import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

total_sum = sum(lst[:k])

max_sum = total_sum
for i in range(k, n):
    total_sum += lst[i] - lst[i - k]
    max_sum = max(max_sum, total_sum)

print(max_sum)
