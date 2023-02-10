import sys

a = list(sys.stdin.readline().strip().upper())

count = {}

for i in a:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

cnt = 0

for j, k in count.items():
    if k == max(count.values()):
        cnt += 1

if cnt >= 2:
    print('?')
else:
    print(max(count, key=count.get))
