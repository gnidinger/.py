import sys

x = int(sys.stdin.readline())

n = 0

while (pow(n, 2) + n) / 2 < x:
    n += 1

i = int(x - (pow(n - 1, 2) + n - 1) / 2)

num = 0
den = 0

if n % 2 != 0:
    num = n - i + 1
    den = i
else:
    num = i
    den = n - i + 1

print(num, "/", den, sep="")
