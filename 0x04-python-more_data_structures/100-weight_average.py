#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    av = 0
    div = 0
    for n in my_list:
        av += n[0] * n[1]
        div += n[1]
    return (float(av/div))
