#!/usr/bin/python3


def b22(j, data):
    return j+1 < len(data) and data[j+1] > 127 \
        and data[j+1] < 192


def validUTF8(data):
    if isinstance(data, list) and len(data):
        ln = len(data)
        j = 0
# redundant comment just to have a commit
        while j < ln:
            b1 = data[j] > 0 and data[j] < 128
            b2 = data[j] > 191 and data[j] < 224 and b22(j, data)
            b3 = data[j] > 223 and data[j] < 240 \
                and b22(j, data) and b22(j+1, data)
            b4 = data[j] > 239 and data[j] < 248 \
                and b22(j, data) \
                and b22(j+1, data) \
                and b22(j+2, data)
            if b1:
                j += 1
                continue
            elif b2:
                j += 2
                continue
            elif b3:
                j += 3
                continue
            elif b4:
                j += 4
                continue
            else:
                return False
        return True
    return False
