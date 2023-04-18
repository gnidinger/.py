import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    ps_list = list(sys.stdin.readline().rstrip())
    if ps_list[0] == ')' or ps_list[-1] == '()':
        print('NO')
        continue
    ps_stack = list()
    for i in ps_list:
        if len(ps_stack) == 0:
            if i == '(':
                ps_stack.append('(')
                continue
            if i == ')':
                ps_stack.append(')')
        elif ps_stack[-1] == '(':
            if i == '(':
                ps_stack.append('(')
            elif i == ')':
                del ps_stack[-1]
        elif ps_stack[-1] == ')':
            if i == '(':
                ps_stack.append('(')
            elif i == ')':
                ps_stack.append(')')
    if len(ps_stack) == 0:
        print('YES')
    else:
        print('NO')
