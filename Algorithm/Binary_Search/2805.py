import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().rstrip().split(' ')))

left = 0
right = max(trees)
answer = 0

while left <= right:
    mid = (left + right) // 2
    sum = 0

    for tree in trees:
        if tree > mid:
            sum += tree - mid

    if sum >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
