import sys

n = int(sys.stdin.readline().rstrip())

a = set()
cnt = 0

for i in range(n):
    x = sys.stdin.readline().rstrip()
    if x == 'ENTER':
        cnt += len(a)
        a = set()
    elif i == n - 1:
        a.add(x)
        cnt += len(a)
    else:
        a.add(x)

print(cnt)
