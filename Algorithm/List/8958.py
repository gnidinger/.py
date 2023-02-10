import sys

a = int(sys.stdin.readline())

for i in range(a):
    b = list(sys.stdin.readline())  # 문자열을 바로 리스트로 변경
    count = 0
    result = 0
    for j in b:
        if j == 'O':
            count += 1
            result += count
        else:
            count = 0
    print(result)
