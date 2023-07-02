#!/usr/bin/python3
""" 00-pascal_triangle """


def pascal_triangle(n):
    """ returns pascal triangle of size n """
    pl = []
    if n > 0:
        for i in range(n):
            sl = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    item = 1
                else:
                    item = prevl[j] + prevl[j - 1]
                sl.append(item)
            pl.append(sl)
            prevl = sl
    return pl
