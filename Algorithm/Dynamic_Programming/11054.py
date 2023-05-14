import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]
result = 1

for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            increase[i] = max(increase[i], increase[j] + 1)

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if lst[j] < lst[i]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

for i in range(n):
    result = max(result, increase[i] + decrease[i] - 1)

print(result)
