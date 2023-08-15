from Sort_Impl.sort_strategy import SortStrategy


class MergeSortStrategy(SortStrategy):
    def sort(self, lst):
        temp = [0] * len(lst)
        self._merge_sort(lst, 0, len(lst) - 1, temp)

    def _merge_sort(self, list, start, end, temp):
        if start >= end:
            return  # 최소단위까지 쪼개면 리턴

        mid = (start + end) // 2  # 주어진 요소의 중간 값을 찾는다

        self._merge_sort(list, start, mid, temp)  # 왼쪽 절반에 대해 재귀호출
        self._merge_sort(list, mid + 1, end, temp)  # 오른쪽 절반에 대해 재귀호출. 왼쪽 절반이 모두 끝난 뒤에 호출된다.

        ########################
        # 쪼개기 끝났으니 합치기 시작 #
        ########################

        left = start  # 왼쪽 조각의 시작점
        right = mid + 1  # 오른쪽 조각의 시작점
        idx = left  # 비교후 temp에 채워넣을 인덱스

        while left <= mid and right <= end:
            ###########################################################
            # 왼쪽 조각의 left번째 요소가 오른쪽 조각의 right번째 요소보다 작을 경우 #
            # temp의 idx에 left번째 요소를 삽입한 뒤 left와 idx += 1         #
            ###########################################################
            if list[left] <= list[right]:
                temp[idx] = list[left]
                idx += 1
                left += 1
            # 반대의 경우 right번째 요소로 동일한 작업 수행
            else:
                temp[idx] = list[right]
                idx += 1
                right += 1
        ###########################################################
        # 왼쪽 조각의 요소가 먼저 떨어졌을 경우(left > mid)                #
        # 오른쪽 조각은 아직 남아있기 때문에 순서대로 나머지를 채워넣는다.        #
        # 비교하지 않고 채워넣는 이유는 모든 조각은 이미 정렬이 끝난 상태이기 때문! #
        ###########################################################
        if left > mid:
            while right <= end:
                temp[idx] = list[right]
                idx += 1
                right += 1
        # 반대의 경우
        else:
            while left <= mid:
                temp[idx] = list[left]
                idx += 1
                left += 1

        # 병합이 모두 끝나면 temp를 리스트에 넣어준다.
        for i in range(start, end + 1):
            list[i] = temp[i]
