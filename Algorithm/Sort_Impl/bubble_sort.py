def bubble_sort(target):
    for i in range(len(target)):
        for j in range(len(target) - 1):
            if target[j] > target[j + 1]:
                temp = target[j]
                target[j] = target[j + 1]
                target[j + 1] = temp


target = [4, 16, 31, 5, 4, 17, 1, 10, 15, 3, 16, 6, 7, 2, 2, 1, 5, 13, 17, 14, 4, 0]

bubble_sort(target)

print(target)
