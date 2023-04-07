import sys

n = int(sys.stdin.readline())
result = [0] * n
target = []

for _ in range(n):
    a = int(sys.stdin.readline())
    target.append(a)

counting = [0] * (max(target) - min(target) + 1)

for i in range(len(target)):
    counting[target[i] - min(target)] += 1

for i in range(1, len(counting)):
    counting[i] += counting[i - 1]

for i in range(len(target) - 1, -1, -1):
    counting[target[i] - min(target)] -= 1
    result[counting[target[i] - min(target)]] = target[i]

print(*result, sep='\n')
