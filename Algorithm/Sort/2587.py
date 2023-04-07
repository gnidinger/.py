import sys

list = []

for i in range(5):
    list.append(int(sys.stdin.readline()))

list.sort()

print(sum(list) // len(list))
print(list[2])
