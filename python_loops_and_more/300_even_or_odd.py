#!/usr/bin/python3
import random
random_num = random.randint(-10000, 10000)
last_digit = abs(random_num) % 10
if last_digit == 0:
    status = 'zero'
elif last_digit % 2 == 0:
    status = 'even'
else:
    status = 'odd'
print(f'{random_num} - the last digit {last_digit} is {status}')

