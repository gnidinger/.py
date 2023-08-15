from Sort_Impl.quick_sort import QuickSortStrategy
from Sort_Impl.merge_sort import MergeSortStrategy
from sorter import Sorter

lst = [4, 16, 31, 5, 4, 17, 1, 10, 15, 3, 16, 6, 7, 2, 2, 1, 5, 13, 17, 14, 4, 0]

sorter = Sorter(QuickSortStrategy())
sorter.sort(lst)
print("Quick Sort: ", lst)

sorter.set_strategy(MergeSortStrategy())
sorter.sort(lst)
print("Merge Sort: ", lst)
