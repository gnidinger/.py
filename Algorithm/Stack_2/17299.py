import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split(" ")))
freq = [0] * 1000001
for num in lst:
    freq[num] += 1

result = [-1] * n

stack = []
stack.append(0)

for i in range(1, n):
    while stack and freq[lst[stack[-1]]] < freq[lst[i]]:
        result[stack.pop()] = lst[i]
    stack.append(i)

print(" ".join(map(str, result)))
