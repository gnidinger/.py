from collections import deque
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    op = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    x = sys.stdin.readline().rstrip()
    if x == '[]':
        x = []
    else:
        x = deque(list(map(int, x.strip('[]').split(','))))

    if n < op.count('D'):
        print('error')
        continue

    rcnt = 0

    for i in op:
        if i == 'R':
            rcnt += 1
        if i == 'D':
            if rcnt % 2 == 0:
                x.popleft()
            else:
                x.pop()

    if rcnt % 2 == 0:
        print('[', end='')
        print(*x, sep=',', end='')
        print(']', end='\n')
    else:
        print('[', end='')
        print(*reversed(x), sep=',', end='')
        print(']')
