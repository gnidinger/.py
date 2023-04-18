from collections import deque
import sys

t = int(sys.stdin.readline().rstrip())


for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    dq = deque(range(n))
    tmp = deque(list(map(int, sys.stdin.readline().rsplit())))

    cnt = 0

    while True:
        maxnum = max(tmp)
        a = tmp.popleft()
        b = dq.popleft()

        if a == maxnum:
            if b == m:
                cnt += 1
                print(cnt)
                break
            else:
                cnt += 1
        else:
            tmp.append(a)
            dq.append(b)
