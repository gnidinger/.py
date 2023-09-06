import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque()

for i in range(10):
    queue.append(i)

num = -1

while 0 <= n and queue:
    num = queue.popleft()
    lastDigit = num % 10

    for i in range(lastDigit):
        queue.append(num * 10 + i)

    n -= 1

if n < 0:
    print(num)
else:
    print(-1)
