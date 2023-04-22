import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

list = list(map(int, sys.stdin.readline().rstrip().split()))
temp = [0] * len(list)

cnt = 0


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    global cnt
    i, j, t = p, q + 1, 0
    tmp = [0] * (r - p + 1)
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            cnt += 1
            if cnt == k:
                print(tmp[t])
                break
            i += 1
        else:
            tmp[t] = A[j]
            cnt += 1
            if cnt == k:
                print(tmp[t])
                break
            j += 1
        t += 1
    while i <= q:
        tmp[t] = A[i]
        cnt += 1
        if cnt == k:
            print(tmp[t])
            break
        i += 1
        t += 1
    while j <= r:
        tmp[t] = A[j]
        cnt += 1
        if cnt == k:
            print(tmp[t])
            break
        j += 1
        t += 1
    A[p : r + 1] = tmp


merge_sort(list, 0, len(list) - 1)

if cnt < k:
    print(-1)
