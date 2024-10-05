#!/usr/bin/python3

def tuple_return(arg):
    if len(arg) == 0:
        return len(arg), None
    else:
        return len(arg), arg[0]

