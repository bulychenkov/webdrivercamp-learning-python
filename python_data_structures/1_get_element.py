#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 2

def print_elt(lst: list, i: int):
    if not 0 <= i < len(lst):
        return None
    print(lst[i])

print_elt(list_, index)

