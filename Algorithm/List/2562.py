import sys

a = []

for i in range(9):
    a.append(int(sys.stdin.readline()))

print(max(a), a.index(max(a)) + 1, sep='\n')

# print(max(a))
# print(a.index(max(a)) + 1)
