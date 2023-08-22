import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
mx = 100000

distance = [-1] * (mx + 1)
distance[n] = 0

queue = deque()
queue.append(n)

while queue:
    current = queue.popleft()

    if current == k:
        print(distance[current])
        quit()

    next_position = [current - 1, current + 1, current * 2]

    for next in next_position:
        if 0 <= next and next <= mx and distance[next] == -1:
            distance[next] = distance[current] + 1
            queue.append(next)
