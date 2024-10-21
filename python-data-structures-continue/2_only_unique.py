#!/usr/bin/python3
def only_unique(list_=[]):
    flt_lst = []
    for n in list_:
        flt_lst += [n] if n not in flt_lst else []
    return sum(flt_lst)

if __name__=="__main__":
    list_ = [0, 1, 6, 3, 6, 4, 0, 2, 5, 4, 4]
    result = only_unique(list_)
    print(f"Sum of unique: {result}")
