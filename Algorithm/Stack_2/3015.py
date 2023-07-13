import sys


class Person:
    def __init__(self, height, count):
        self.height = height
        self.count = count


n = int(sys.stdin.readline().rstrip())
stack = []
result = 0

for _ in range(n):
    height = int(sys.stdin.readline().rstrip())
    count = 1

    while stack:
        if stack[-1].height <= height:
            result += stack[-1].count
            if stack[-1].height == height:
                count += stack[-1].count
            stack.pop()
        else:
            break

    if stack:
        result += 1

    stack.append(Person(height, count))

print(result)
