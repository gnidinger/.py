from collections import deque
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

dq = deque([i + 1 for i in range(n)])


print('<', end='')

while True:
    if len(dq) == 1:
        print(dq[0], end='')
        break

    for _ in range(k - 1):
        dq.append(dq.popleft())

    print(dq.popleft(), end=', ')

print('>', end='')
