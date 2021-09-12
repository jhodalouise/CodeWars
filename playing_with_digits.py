n = 1
p = 400


def dig_pow(n, p):
    str_n = str(n)
    total = 0
    for i in str_n:
        i = int(i)
        total += (i ** p)
        p += 1

    if total >= n:
        k = total / n
        if k.is_integer():
            return k
        else:
            return -1
    else:
        return -1

print(dig_pow(n, p))
