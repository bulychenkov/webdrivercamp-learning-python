#!/usr/bin/python3

def fizz_buzz(i: int):
    if i % 3 == 0 and i % 5 == 0:
        res = 'FizzBuzz'
    elif i % 3 == 0:
        res = 'Fizz'
    elif i % 5 == 0:
        res = 'Buzz'
    else:
        res = f'{i}'
    return res


for i in range(1, 101):
    if i != 100:
        print(fizz_buzz(i), end=' ')
    else:
        print(fizz_buzz(i))

