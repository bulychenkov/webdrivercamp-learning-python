#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]
res = tuple(not bool(elt % 2) for elt in my_list)
print(my_list)
print(res)

