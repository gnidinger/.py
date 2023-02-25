import sys

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = sys.stdin.readline().rstrip()

duration = 0

for i in dial:
    for j in i:
        for k in a:
            if j == k:
                duration += dial.index(i) + 3

print(duration)
