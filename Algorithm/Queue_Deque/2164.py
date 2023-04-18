from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

queue = deque([i + 1 for i in range(n)])


while True:
    if len(queue) == 1:
        print(queue[0])
        break

    queue.popleft()
    queue.append(queue.popleft())
