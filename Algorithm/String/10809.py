import sys

a = list(sys.stdin.readline().strip())

b = []

for i in range(26):
    if chr(i + 97) in a:
        b.append(a.index(chr(i + 97)))
    else:
        b.append(-1)

print(*b)
