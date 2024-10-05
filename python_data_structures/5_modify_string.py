#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""

def remove_char(some_string):
    new_str = ''
    for c in some_string:
        new_str += c if not c == 'a' or c == 'A' else ''
    return new_str

print(remove_char(string))

