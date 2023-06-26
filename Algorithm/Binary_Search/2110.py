import sys

n, c = map(int, sys.stdin.readline().rstrip().split())
houses = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

houses = sorted(houses)

left = 1
right = houses[n - 1] - houses[0]
answer = 0

while left <= right:
    mid = (left + right) // 2
    start = houses[0]
    count = 1

    for house in houses:
        distance = house - start
        if distance >= mid:
            count += 1
            start = house

    if count >= c:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
