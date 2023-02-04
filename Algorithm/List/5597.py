import sys

result = []

for i in range(30):
    result.append(i + 1)

for i in range(28):
    result.remove(int(sys.stdin.readline()))

print(min(result), max(result), sep='\n')
