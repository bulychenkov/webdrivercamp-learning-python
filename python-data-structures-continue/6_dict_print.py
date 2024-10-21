#!/usr/bin/python3
def dict_print(dict_):
    for k in sorted(dict_):
        print(f'{k}: {dict_[k]}')

if __name__=="__main__":
    dict_ = {"libs": (1,2,3), "x": "Selenium", "lang": ["Java", "Python"], "frame": "Behave", "set": set()}
    dict_print(dict_)
