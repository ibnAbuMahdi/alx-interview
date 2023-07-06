#!/usr/bin/python3
""" 0-lockboxes """


def canUnlockAll(boxes):
    """ determines if all boxes can be unlocked """
    cp = [boxes[0]];

    for box in cp:
        for n in box:
            if n < len(boxes) and boxes[n] not in cp:
                cp.append(boxes[n])
    return len(cp) == len(boxes)
