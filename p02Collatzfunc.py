
def collatz(i):
    ncount = 0
    while i != 1:
        if i% 2 == 1:
            i = 3 * i +1
        else:
            i = i/2
        ncount = ncount + 1
    return ncount

def find_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for num in lst[1:]:
        if num > max_value:
            max_value = num
    return max_value

def top_collatz_counts(limit=101):
    f_max = max_n1 = 0
    s_max = max_n2 = 0
    t_max = max_n3 = 0

    for n in range(1, limit):
        count = 0
        i = n
        while i != 1:
            if i % 2 == 1:
                i = 3 * i + 1
            else:
                i = i / 2
            count += 1

        if count > f_max:
            t_max, max_n3 = s_max, max_n2
            s_max, max_n2 = f_max, max_n1
            f_max, max_n1 = count, n
        elif count > s_max:
            t_max, max_n3 = s_max, max_n2
            s_max, max_n2 = count, n
        elif count > t_max:
            t_max, max_n3 = count, n

    return {
        '1st': (max_n1, f_max),
        '2nd': (max_n2, s_max),
        '3rd': (max_n3, t_max)
    }