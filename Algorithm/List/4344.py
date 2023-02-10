import sys

c = int(sys.stdin.readline())

result = []

for i in range(c):
    total = list(map(int, sys.stdin.readline().split()))
    number = total[0]
    score = total[1:]
    average = sum(score) / number
    count = 0
    for j in score:
        if j > average:
            count += 1
    result.append(count * 100 / number)

result = [f'{i:.3f}%' for i in result]

print(*result, sep='\n')
