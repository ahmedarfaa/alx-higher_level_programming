#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolst = my_list[:]
    for cou, i in enumerate(my_list):
        if i % 2 == 0:
            boolst[cou] = True
        else:
            boolst[cou] = False
    return(boolst)
