import sys

expression = sys.stdin.readline().rstrip()

total = 0
sub_total = 0
is_subtract = False

for i, ch in enumerate(expression):
    if ch == '+' or ch == '-':
        total += -sub_total if is_subtract else sub_total
        sub_total = 0

        if ch == '-':
            is_subtract = True

    else:
        sub_total = sub_total * 10 + int(ch)

total += -sub_total if is_subtract else sub_total

print(total)
