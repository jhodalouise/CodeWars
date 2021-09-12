a = [0,1,2]
b = [9,8,7,6,5,4,3,2,1,0]


def compound_array(a, b):
    result = []

    len_a = len(a)
    len_b = len(b)

    if len_a < len_b:
        for i in range(0, len_a):
            result.append(a[i])
            result.append(b[i])
        for i in range(len_a, len_b):
            result.append(b[i])
    else:
        for i in range(0, len_b):
            result.append(a[i])
            result.append(b[i])
        for i in range(len_b, len_a):
            result.append(a[i])

    return result


print(compound_array(a, b))
