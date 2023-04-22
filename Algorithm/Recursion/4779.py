import sys

lst = list()


def cantor(ex):
    global lst

    if len(ex) == 1:
        lst.append(ex[0])
    else:
        cantor(ex[0 : len(ex) // 3])
        cantor(ex[len(ex) * 2 // 3 : len(ex)])


while True:
    try:
        n = int(sys.stdin.readline().rstrip())
        ex = [i for i in range(0, 3**n)]
        lst = []
        result = [' '] * (3**n)

        cantor(ex)

        for i in lst:
            result[i] = '-'

        print(*result, sep='')

    except:
        break
