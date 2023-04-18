from collections import deque
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

dq = deque(range(1, n + 1))

num = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0

for i in range(m):
    index = dq.index(num[i])
    count = min(index, len(dq) - index)
    cnt += count

    dq.rotate(-index)
    dq.popleft()

print(cnt)
