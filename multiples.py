def solution(number):
    multiples = list()
    m = number-1
    while (m > 0):
        if m%3 == 0 or m%5 == 0:
            multiples.append(m)
            m -= 1
        else:
            m -= 1

    if len(multiples) > 0:
        return sum(multiples)
    else:
        return 0

print(solution(10))


# Cool solution
number = 10
print(sum([x for x in range(number) if x % 3 == 0 or x % 8 == 0]))
