import sys

n = sys.stdin.readline().strip()


def octal_to_binary(octal):
    binary = ""
    for digit in octal:
        binary += format(int(digit, 8), "03b")
    return binary


result = octal_to_binary(n)

for i in range(len(result)):
    if result[i] == "1":
        print(result[i:])
        break
    if i == len(result) - 1:
        print("0")
