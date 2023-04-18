x = [1, 2, 3, 4, 5]

print('[', end='')
print(*reversed(x), sep=',', end='')
print(']')
