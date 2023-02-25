a = input()

b = len(a)

for i in range(b):
    if a[i] == '=' and (a[i - 1] == 'z' and a[i - 2] == 'd'):
        b -= 1
    if a[i] == '=' and (a[i - 1] == 'c' or a[i - 1] == 's' or a[i - 1] == 'z'):
        b -= 1
    if a[i] == '-' and (a[i - 1] == 'c' or a[i - 1] == 'd'):
        b -= 1
    if a[i] == 'j' and (a[i - 1] == 'l' or a[i - 1] == 'n'):
        b -= 1

print(b)
