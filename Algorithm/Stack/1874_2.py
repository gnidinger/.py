import sys

n = int(sys.stdin.readline().rstrip())

stack = []
result = []
cnt = 0

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())

    if len(stack) == 0:
        m = num - cnt
        for i in range(m - 1, -1, -1):
            stack.append(num - i)
            result.append('+')
        result.append('-')
        cnt += 1
        stack.pop()

    else:
        if num < stack[-1]:
            print('NO')
            sys.exit()
        elif num == stack[-1]:
            result.append('-')
            cnt += 1
            stack.pop()
        elif num > stack[-1]:
            m = num - len(stack) - cnt
            for i in range(m - 1, -1, -1):
                stack.append(num - i)
                result.append('+')
            result.append('-')
            cnt += 1
            stack.pop()

print(*result, sep='\n')
