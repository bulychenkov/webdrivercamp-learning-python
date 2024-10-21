#!/usr/bin/python3
def calc_weight(list_=[]):
    if len(list_) == 0:
        return 0
    return sum([e[0]*e[1] for e in list_])/sum([e[1] for e in list_])

if __name__=="__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
