#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    my_list = dir(hidden_4)
    for name in my_list:
        if name[0:2] != '__':
            print("{}".format(name))
