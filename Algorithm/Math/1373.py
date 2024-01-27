import sys

binary = sys.stdin.readline().strip()
binary = "0b" + binary

decimal = int(binary, 2)
octal = oct(decimal)[2:]

print(octal)
