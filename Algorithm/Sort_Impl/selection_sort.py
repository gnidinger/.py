def selection_sort(target):
    for i in range(len(target) - 1):
        min = target[i]
        minidx = i

        for j in range(i + 1, len(target)):
            if target[j] < min:
                min = target[j]
                minidx = j

        temp = target[i]
        target[i] = target[minidx]
        target[minidx] = temp


target = [4, 16, 31, 5, 4, 17, 1, 10, 15, 3, 16, 6, 7, 2, 2, 1, 5, 13, 17, 14, 4, 0]

selection_sort(target)

print(target)
