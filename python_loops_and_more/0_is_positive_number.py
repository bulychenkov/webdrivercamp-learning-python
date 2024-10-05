#!/usr/bin/python3
import random
random_num = random.randint(-10, 10)
if random_num > 0:
    status = 'positive'
elif random_num < 0:
    status = 'negative'
else:
    status = 'zero'
print(f'{random_num} is {status}')
