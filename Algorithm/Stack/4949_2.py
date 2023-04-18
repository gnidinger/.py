import sys

result = list()

while True:
    stack = list()
    a = list(sys.stdin.readline().rstrip())
    if a[0] == '.':
        break
    for i in a:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                result.append('NO')
                break
            elif stack[-1] == '[':
                result.append('NO')
                break
            elif stack[-1] == '(':
                del stack[-1]
        elif i == ']':
            if len(stack) == 0:
                result.append('NO')
                break
            elif stack[-1] == '(':
                result.append('NO')
                break
            elif stack[-1] == '[':
                del stack[-1]
    else:
        if len(stack) == 0:
            result.append('YES')
        else:
            result.append('NO')

print(*result, sep='\n')
