import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split(' ')))
lst = sorted(lst)
m = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split(' ')))

result = ''

for number in numbers:
    isFound = False
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == number:
            isFound = True
            break
        elif lst[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    result += str(1 if isFound else 0) + '\n'

print(result)
