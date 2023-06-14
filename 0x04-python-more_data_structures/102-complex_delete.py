#!/usr/bin/python3
def complex_delete(my_dict, value):
    targets = []
    for key, key_value in my_dict.items():
        if key_value is value:
            targets.append(key)
    for i in targets:
        del my_dict[i]
    return(my_dict)
