import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

inc_len, dec_len, max_len = 1, 1, 1

for i in range(1, n):
    if arr[i] > arr[i - 1]:
        inc_len += 1
        dec_len = 1
    elif arr[i] < arr[i - 1]:
        dec_len += 1
        inc_len = 1
    else:
        inc_len += 1
        dec_len += 1

    max_len = max(max_len, inc_len, dec_len)

sys.stdout.write(str(max_len))
