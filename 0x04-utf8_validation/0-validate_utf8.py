#!/usr/bin/python3
""" utf8 validation module """


def b22(j, data):
    """ checks byte value in range """
    return j+1 < len(data) and data[j+1] > 127 \
        and data[j+1] < 192


def validUTF8(data):
    """ checks data is a valid utf8 code """
    if isinstance(data, list) and len(data) and isinstance(data[0], int):
        ln = len(data)
        j = 0
        while j < ln:
            b1 = data[j] >= 0 and data[j] < 128
            b2 = data[j] > 192 and data[j] < 224 and b22(j, data)
            b3 = data[j] > 224 and data[j] < 240 \
                and b22(j, data) and b22(j+1, data)
            b4 = data[j] > 240 and data[j] < 248 \
                and b22(j, data) \
                and b22(j+1, data) \
                and b22(j+2, data)
            if b1:
                j += 1
            elif b2:
                j += 2
            elif b3:
                j += 3
            elif b4:
                j += 4
            else:
                return False
        return True
    return False
