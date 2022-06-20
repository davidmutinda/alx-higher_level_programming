#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as err:
        sys.stderr.write("Exception: " + str(err) + "\n")
    else:
        return True
    return False
