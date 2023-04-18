from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

queue = deque()

for _ in range(n):
    order = sys.stdin.readline().rstrip()

    if 'push' in order:
        a, b = order.split()
        queue.appendleft(b)

    elif order == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
            del queue[-1]

    elif order == 'size':
        print(len(queue))

    elif order == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif order == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[-1])

    elif order == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[0])
