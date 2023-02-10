a = list(i + 1 for i in range(10000))

# fmt: off
for i in range(1, 10001):
    b = ((i % 10000) // 1000 
    + (i % 1000) // 100
    + (i % 100) // 10 
    + i % 10 
    + i)

    if b in a:
        a.remove(b)

print(*a, sep='\n')
