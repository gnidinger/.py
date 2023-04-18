import sys

n = int(sys.stdin.readline().rstrip())

result = []

for _ in range(n):
    a = sys.stdin.readline().rstrip()

    if 'push_front' in a:
        m, n = a.split()
        result.insert(0, n)
    elif 'push_back' in a:
        m, n = a.split()
        result.append(n)
    elif 'pop_front' in a:
        if not result:
            print(-1)
        else:
            print(result[0])
            del result[0]
    elif 'pop_back' in a:
        if not result:
            print(-1)
        else:
            print(result[-1])
            del result[-1]
    elif a == 'size':
        print(len(result))
    elif a == 'empty':
        if not result:
            print(1)
        else:
            print(0)
    elif a == 'front':
        if not result:
            print(-1)
        else:
            print(result[0])
    elif a == 'back':
        if not result:
            print(-1)
        else:
            print(result[-1])
