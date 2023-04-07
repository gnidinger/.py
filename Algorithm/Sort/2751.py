import sys

n = int(sys.stdin.readline())
list = []
temp = [0] * n

for _ in range(n):
    list.append(int(sys.stdin.readline()))


def merge_sort(list, start, end):
    if start == end:
        return

    mid = (start + end) // 2

    merge_sort(list, start, mid)
    merge_sort(list, mid + 1, end)

    left = start
    right = mid + 1
    idx = left

    while left <= mid and right <= end:
        if list[left] <= list[right]:
            temp[idx] = list[left]
            idx += 1
            left += 1
        else:
            temp[idx] = list[right]
            idx += 1
            right += 1
    if left > mid:
        while right <= end:
            temp[idx] = list[right]
            idx += 1
            right += 1
    else:
        while left <= mid:
            temp[idx] = list[left]
            idx += 1
            left += 1

    for i in range(start, end + 1):
        list[i] = temp[i]


merge_sort(list, 0, len(list) - 1)

print(*list, sep='\n')
