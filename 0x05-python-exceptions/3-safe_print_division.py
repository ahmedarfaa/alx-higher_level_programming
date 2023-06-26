#!/usr/bin/pyhton3
def safe_print_division(a, b):
    try:
        res = a / b
        print("Inside result: {:.1f}".format(res))
    except (TypeError, ZeroDivisionError):
        res = None
        print("Inside result: {}".format(res))
    finally:
        return (res)
