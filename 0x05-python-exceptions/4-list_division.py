#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i]/my_list_2[i])
        except TypeError:
            print("{}".format("wrong type"))
            new_list.append(0)
            pass
        except ZeroDivisionError:
            print("{}".format("division by 0"))
            new_list.append(0)
            pass
        except IndexError:
            print("{}".format("out of range"))
            new_list.append(0)
        finally:
            pass
    return new_list
