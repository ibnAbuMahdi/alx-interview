#!/usr/bin/python3
""" 101-nqueens.py """


from sys import exit, argv as av
if len(av) != 2:
    print("Usage: nqueens N")
    exit(1)

if not str.isdigit(av[1]):
    print("N must be a number")
    exit(1)

N = int(av[1])

if N < 4:
    print("N must be at least 4")
    exit(1)

# initialize solution list, start column, occupied columns list,
# occupied left diagonal list and occupied right diagonal list
sol = []
i = j = st = 0
col = []
ldiag = []
rdiag = []

# loop for  rows
while i < N:

    # loop for columns
    while j < N:

        # cell coordinates for rdiag
        cc = min(j + i, N)
        rc = max(0, i - (N - j))

        # check for similar column, rdiag or ldiag
        if j not in col and i - j not in ldiag and [rc, cc] not in rdiag:
            ldiag.append(i - j)
            rdiag.append([rc, cc])
            col.append(j)
            sol.append([i, j])
            j = 0
            break
        j += 1

    # if a solution is found, backtrack to the first row and next column
    if len(sol) == N:
        print(sol)
        top = sol.pop()
        col.remove(top[1])
        ldiag.pop()
        rdiag.pop()
        ln = len(sol)
    """        j = sol[0][1] + 1
        i = 0
        sol.clear()
        ldiag.clear()
        rdiag.clear()
        col.clear()
    """
    # if next valid position is not found, backtrack to the previous
    # queen and move it to the next column and same row and delete
    # all its diags and column
    if i > 0 and len(sol) > 0 and len(sol) == ln:
        top = sol.pop()
        j = top[1] + 1
        i -= 1
        col.remove(top[1])
        ldiag.pop()
        rdiag.pop()
        ln -= 1

    # else, i.e. a valid position is found, update ln
    else:
        i += 1
        ln = len(sol)
