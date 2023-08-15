def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def heap_sort(lst, l):
    if l == 0:
        return

    for i in range(1, l):
        while i != 0:
            parent = (i - 1) // 2

            if lst[parent] < lst[i]:
                swap(lst, parent, i)
            else:
                break

            i = parent

    swap(lst, 0, l - 1)

    heap_sort(lst, l - 1)


lst = [4, 16, 31, 5, 4, 17, 1, 10, 15, 3, 16, 6, 7, 2, 2, 1, 5, 13, 17, 14, 4, 0]
l = len(lst)

heap_sort(lst, l)

print(lst)
