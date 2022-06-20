#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    i = 0
    while list_length:
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]

        except (ValueError, TypeError):
            print("Wrong type")

        except ZeroDivisionError:
            print("division by zero")

        except IndexError:
            print("out of range")

        finally:
            result.append(div)

        list_length -= 1
        i += 1
    return result
