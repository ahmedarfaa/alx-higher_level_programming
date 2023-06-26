#!/usr/bin/python3
def magic_calculation(a, b):
    magc = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                magc += (a ** b) / i
        except Exception:
            magc = b + a
            break
    return (magc)
