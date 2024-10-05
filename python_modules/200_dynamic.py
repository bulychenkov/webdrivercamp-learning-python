#!/usr/bin/python3
from sys import argv

separator = '.' if len(argv) == 1 else ':'
word = 'argument' if len(argv) == 2 else 'arguments'
print(f'{len(argv) - 1} {word}{separator}')

for i in range(1, len(argv)):
    print(f'{i}: {argv[i]}')

