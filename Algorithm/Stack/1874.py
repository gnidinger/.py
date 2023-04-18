import sys

n = int(sys.stdin.readline().rstrip())

stack = []
result = []

for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    if len(stack) == 0:
        m = a - result.count('-')
        for i in range(m - 1, 0 - 1, -1):
            stack.append(a - i)
            result.append('+')
        result.append('-')
        stack.pop()
    else:
        if a < stack[-1]:
            print('NO')
            sys.exit()
        elif a == stack[-1]:
            result.append('-')
            stack.pop()
        elif a > stack[-1]:
            m = a - len(stack) - result.count('-')
            for i in range(m - 1, 0 - 1, -1):
                stack.append(a - i)
                result.append('+')
            result.append('-')
            stack.pop()

print(*result, sep='\n')
