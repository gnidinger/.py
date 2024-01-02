import sys

m = int(input())
n = int(input())

min_square = None
sum_of_squares = 0

for num in range(1, 101):
    square = num * num
    if m <= square <= n:
        sum_of_squares += square
        if min_square is None:
            min_square = square

if min_square is None:
    print(-1)
else:
    print(sum_of_squares)
    print(min_square)
