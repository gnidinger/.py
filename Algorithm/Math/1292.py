import sys

a, b = map(int, input().split())

sequence = []
for i in range(1, 46):
    sequence.extend([i] * i)

result = sum(sequence[a - 1 : b])
print(result)
