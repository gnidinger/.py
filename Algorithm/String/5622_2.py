import sys

a = sys.stdin.readline().rstrip()

duration = 0

for i in a:
    if 0 <= ord(i) <= 79:
        duration += (ord(i) - 65) // 3 + 3
    else:
        if i in 'PQRS':
            duration += 8
        elif i in 'TUV':
            duration += 9
        else:
            duration += 10

print(duration)
