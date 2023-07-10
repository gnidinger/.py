import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split(" ")))
result = [-1] * n

stack = []
stack.append(0)

for i in range(1, n):
    while stack and lst[stack[-1]] < lst[i]:
        result[stack.pop()] = lst[i]
    stack.append(i)

print(" ".join(map(str, result)))
