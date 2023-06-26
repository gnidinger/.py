import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split(' ')))

lis = [0] * n
result = 0

for i in range(n):
    left = 0
    right = result

    while left < right:
        mid = (left + right) // 2

        if lis[mid] < numbers[i]:
            left = mid + 1
        else:
            right = mid

    lis[left] = numbers[i]

    if left == result:
        result += 1

print(result)
