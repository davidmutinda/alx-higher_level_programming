def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except (ZeroDivisionError, ValueError, TypeError, IndexError) as err:
        sys.stderr.write("Exception: " + str(err) + "\n")
        return None
