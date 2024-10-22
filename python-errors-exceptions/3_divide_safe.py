#!/usr/bin/python3
def divide_safe(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        c = None
    finally:
        print(f'Result: {c}')
    return c

if __name__ == "__main__":
    a = 9
    b = 3
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")

    b = 0
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
