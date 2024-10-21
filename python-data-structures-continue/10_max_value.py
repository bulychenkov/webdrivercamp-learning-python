#!/usr/bin/python3
def max_value(d):
    if d is None:
        return None

    max_key = None
    max_val = float('-inf')
    for key, val in d.items():
        if val > max_val:
            max_val = val
            max_key = key
    return max_key

if __name__=="__main__":
    dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
    max_key = max_value(dict_)
    print(f"Max number - {max_key}")

    max_key = max_value(None)
    print(f"Max number - {max_key}")
