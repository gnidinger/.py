import sys

score = 0.0
count = 0

for i in range(20):
    a, b, c = sys.stdin.readline().split()

    b = float(b)

    if c == 'P':
        continue
    elif c == 'F':
        count += b
    elif c == 'A+':
        score += b * 4.5
        count += b
    elif c == 'A0':
        score += b * 4.0
        count += b
    elif c == 'B+':
        score += b * 3.5
        count += b
    elif c == 'B0':
        score += b * 3.0
        count += b
    elif c == 'C+':
        score += b * 2.5
        count += b
    elif c == 'C0':
        score += b * 2.0
        count += b
    elif c == 'D+':
        score += b * 1.5
        count += b
    elif c == 'D0':
        score += b * 1.0
        count += b

print(score / count)
