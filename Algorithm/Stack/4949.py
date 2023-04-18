import sys

while True:
    stack = list()
    a = list(sys.stdin.readline().rstrip())
    if len(a) == 1 and a[0] == '.':
        break
    for i in a:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                print('no')
                break
            elif stack[-1] == '[':
                print('no')
                break
            elif stack[-1] == '(':
                del stack[-1]
        elif i == ']':
            if len(stack) == 0:
                print('no')
                break
            elif stack[-1] == '(':
                print('no')
                break
            elif stack[-1] == '[':
                del stack[-1]
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')
