import sys

n = int(sys.stdin.readline().rstrip())
lst = []

for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))

lst = sorted(lst, key=lambda x: x[1])

cnt = 1
end_time = lst[0][1]

for i in range(1, n):
    if lst[i][0] >= end_time:
        cnt += 1
        end_time = lst[i][1]

print(cnt)
