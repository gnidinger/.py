import sys

while True:
    n, *height = map(int, sys.stdin.readline().rstrip().split())

    if n == 0:
        break

    height.append(0)
    stack = []
    max_area = 0

    for i in range(n + 1):
        while stack and height[stack[-1]] > height[i]:
            h = height[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    print(max_area)
