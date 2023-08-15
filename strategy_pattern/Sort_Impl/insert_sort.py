def insert_sort(list):
    for i in range(1, len(list)):
        tmp = list[i]  # 정렬 대상
        j = i - 1  # 바로 왼쪽부터 비교
        while j >= 0 and tmp < list[j]:  # 리스트의 0번에 닿거나 자신보다 작은 요소를 만날 때까지
            list[j + 1] = list[j]  # 비교가 끝난 요소를 오른쪽으로 밀어냄
            j -= 1  # 다음 요소와 비교
        list[j + 1] = tmp  # 자리를 찾으면 삽입


list = [4, 2, 5, 4, 3, 1, 10, 3]

insert_sort(list)

print(list)
