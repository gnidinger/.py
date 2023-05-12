target = [4, 16, 31, 5, 4, 17, 1, 10, 15, 3, 16, 6, 7, 2, 2, 1, 5, 13, 17, 14, 4, 0]


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def partition_step(lst, lo, hi):
    left = lo
    right = hi
    pivot = lst[lo]

    while left < right:
        # pivot 보다 작은 값을 만날 때까지 right -= 1;
        while lst[right] >= pivot and left < right:
            right -= 1
        # pivot 보다 큰 값을 만날 때까지 left += 1;
        while lst[left] <= pivot and left < right:
            left += 1
        # 값을 찾으면 스왑. 못 찾으면 left = right 인 곳에서 자체 스왑
        swap(lst, left, right)

    # left = right 인 원소와 pivot 교환
    swap(lst, lo, left)
    # pivot 이 옯겨간, 즉 정렬된 곳의 인덱스 반환
    return left


def quick_sort(lst, lo, hi):
    # 대상 배열의 크기가 1 이하일 경우 탈출
    if lo >= hi:
        return

    # Partition Step 진행
    pivot = partition_step(lst, lo, hi)

    # 정렬이 끝난 pivot 기준으로 배열 쪼개서 재귀호출(왼쪽)
    quick_sort(lst, lo, pivot - 1)
    # 정렬이 끝난 pivot 기준으로 배열 쪼개서 재귀호출(오른쪽)
    quick_sort(lst, pivot + 1, hi)


quick_sort(target, 0, len(target) - 1)

print(target)
