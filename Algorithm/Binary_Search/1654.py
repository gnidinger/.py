import sys

k, n = map(int, sys.stdin.readline().rstrip().split())
length_lst = [int(sys.stdin.readline().rstrip()) for _ in range(k)]

left = 1
right = max(length_lst)
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for i in range(k):
        cnt += length_lst[i] // mid

    if cnt >= n:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)
