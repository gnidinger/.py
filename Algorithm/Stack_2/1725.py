import sys

n = int(sys.stdin.readline().rstrip())
height = [int(sys.stdin.readline().rstrip()) for _ in range(n)] + [0]
stack = []
result = 0

for i in range(n + 1):
    while stack and height[stack[-1]] >= height[i]:
        h = height[stack.pop()]
        w = 0

        if not stack:
            w = i
        else:
            w = i - stack[-1] - 1

        result = max(result, h * w)

    stack.append(i)

print(result)
