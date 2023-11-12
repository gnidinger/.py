import sys

n = int(sys.stdin.readline().rstrip())

if n == 1 or n == 3:
    print(-1)
elif n % 5 == 0:
    print(n // 5)
else:
    cnt = 0
    while n >= 0:
        if n % 5 == 0:
            cnt += n // 5
            print(cnt)
            break
        n -= 2
        cnt += 1
    else:
        print(-1)
