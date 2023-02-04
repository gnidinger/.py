import sys

result = set()

for i in range(10):
    result.add(int(sys.stdin.readline()) % 42)

print(len(result))
