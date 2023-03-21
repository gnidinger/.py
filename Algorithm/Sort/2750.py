import sys


def insert_sort(list):
    for i in range(1, len(list)):
        tmp = list[i]
        j = i - 1
        while j >= 0 and tmp < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = tmp


n = int(sys.stdin.readline())

list = []

for i in range(n):
    list.append(int(sys.stdin.readline()))

insert_sort(list)

print(*list, sep='\n')
