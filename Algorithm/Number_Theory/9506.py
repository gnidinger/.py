import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    perfect = 0
    list = []
    for i in range(1, n):
        if n % i == 0:
            perfect += i
            list.append(i)
    if perfect == n:
        print(str(n) + ' = ', end='')
        print(*list, sep=' + ')
    else:
        print(str(n) + ' is NOT perfect.')
