#!/usr/bin/python3


def validUTF8(data):
    if isinstance(data, list) and len(data):
        l = len(data)
        j = 0
        b22 = lambda i, ls: i+1 < len(ls) and ls[i+1] > 127 \
            and ls[i+1] < 192
        b1 = lambda i, dat: dat[i] > 0 and dat[i] < 128
        b2 = lambda i, dat: dat[i] > 191 and dat[i] < 224 and b22(i, dat)
        b3 = lambda i, dat: dat[i] > 223 and dat[i] < 240 \
            and b22(i, dat) and b22(i+1, dat)
        b4 = lambda i, dat: dat[i] > 239 and dat[i] < 248 \
            and b22(i, dat) \
            and b22(i+1, dat) \
            and b22(i+2, dat)

        while j < l:
            if b1(j, data):
                j += 1
                continue
            elif b2(j, data):
                j += 2
                continue
            elif b3(j, data):
                j += 3
                continue
            elif b4(j, data):
                j += 4
                continue
            else:
                return False
        return True
    return False
