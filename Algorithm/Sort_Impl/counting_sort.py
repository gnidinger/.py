target = [4, 16, 31, 5, 4, 17, 1, 10, 15, 3, 16, 6, 7, 2, 2, 1, 5, 13, 17, 14, 4, 0]


def counting_sort(target):
    counting = [0 for _ in range(max(target) + 1)]
    result = [0 for _ in range(len(target))]

    for i in range(len(target)):  # 리스트를 순회하며 요소 카운트 후 counting에 입력
        counting[target[i]] += 1

    for i in range(1, len(counting)):  # counting 리스트를 누적합 배열로 변환
        counting[i] += counting[i - 1]

    for i in range(len(target) - 1, -1, -1):  # 마지막 인덱스부터 거꾸로 순회
        counting[target[i]] -= 1  # 해당 인덱스의 값을 -1 해주고
        result[counting[target[i]]] = target[i]  # 줄어든 값을 인덱스로 삼아 result 리스트에 입력

    return result


print(counting_sort(target))
