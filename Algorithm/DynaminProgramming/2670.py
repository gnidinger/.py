import sys

n = int(sys.stdin.readline().rstrip())
numbers = [float(sys.stdin.readline().rstrip()) for _ in range(n)]

max_product = current_product = numbers[0]

for i in range(1, n):
    current_product = max(numbers[i], numbers[i] * current_product)
    max_product = max(max_product, current_product)

print("{:.3f}".format(max_product))
