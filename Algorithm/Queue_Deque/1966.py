from queue import PriorityQueue
import sys

t = int(sys.stdin.readline().rstrip())

prq = PriorityQueue()

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    tmp = list(map(int, sys.stdin.readline().rsplit()))

    for i in range(n):
        prq.put(((-1) * tmp[i], i))

    cnt = 0

    while True:
        x = prq.get()[1]
        if x == m + 1:
            print(cnt)
            break
        else:
            cnt += 1
