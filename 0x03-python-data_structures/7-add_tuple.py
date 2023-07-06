#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    if len(a) == 0:
        a = [0, 0]
    if len(b) == 0:
        b = [0, 0]
    if len(a) == 1:
        a.append(0)
    if len(b) == 1:
        b.append(0)
    return (a[0] + b[0], a[1] + b[1])
    """
    def add_tuple(tuple_a=(0, 0), tuple_b=(0, 0)):
        x1, y1 = tuple_a
        x2, y2 = tuple_b
        return (x1 + x2, y1 + y2)
    """
