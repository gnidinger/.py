import sys


def push(list, x):
    list.append(x)


def pop(list):
    if len(list) == 0:
        print(-1)
    else:
        print(list[-1])
        del list[-1]


def size(list):
    print(len(list))


def empty(list):
    if len(list) == 0:
        print(1)
    else:
        print(0)


def top(list):
    if len(list) == 0:
        print(-1)
    else:
        print(list[-1])


n = int(sys.stdin.readline().rstrip())

stack_list = list()

for _ in range(n):
    a = sys.stdin.readline().rstrip()
    if 'push' in a:
        x, y = a.split()
        push(stack_list, y)
    elif a == 'pop':
        pop(stack_list)
    elif a == 'size':
        size(stack_list)
    elif a == 'empty':
        empty(stack_list)
    elif a == 'top':
        top(stack_list)
