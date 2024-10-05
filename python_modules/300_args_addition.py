#!/usr/bin/python3
from sys import argv

sum = 0
for i in range(1, len(argv)):
    try:
        sum += int(argv[i])
    except:
        continue
print(sum)

