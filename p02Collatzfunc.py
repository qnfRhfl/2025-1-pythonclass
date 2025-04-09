
def collatz(i):
    ncount = 0
    while i != 1:
        if i% 2 == 1:
            i = 3 * i +1
        else:
            i = i/2
        ncount = ncount + 1
    return ncount