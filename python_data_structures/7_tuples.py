#!/usr/bin/python3

# it is a dirty hack :)
def tuple_addition(a = (), b = ()):
    a_, b_ = [], []
    for i in range(2):
        try:
            a_ += [a[i]]
        except:
            a_ += [0]
        try:
            b_ += [b[i]]
        except:
            b_ += [0]
    return a_[0] + b_[0], a_[1] + b_[1]

