#!/usr/bin/pyhton3
def safe_print_division(a, b):
    try:
        div = a / b
        print("Inside result: {}".format(div))
    except (TypeError, ZeroDivisionError):
        div = None
        print("Inside result: {}".format(div))
    finally:
        return (div)
