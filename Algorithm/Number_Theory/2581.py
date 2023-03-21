import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

list = []

for i in range(m, n + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        list.append(i)

if len(list) == 0:
    print(-1)
else:
    print(sum(list))
    print(list[0])
