#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

def replace_elt():
    if 0 <= index < len(list_):
        list_[index] = element_to_replace
    print(list_)

replace_elt()

