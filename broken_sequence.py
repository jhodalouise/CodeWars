sequence = "1"

def find_missing_number(sequence):
    n = sequence.replace(' ','')
    if len(n) == 0:
        return 0
    elif n.isnumeric():
        numbers = sequence.split()
        sorted_numbers = sorted(list(map(int, numbers)))
        first_number = sorted_numbers[0]
        if first_number == 1:
            for n in sorted_numbers:
                if len(sorted_numbers) == 1:
                    return 1
                elif n == max(sorted_numbers):
                    continue
                elif n+1 in sorted_numbers:
                    continue
                else:
                    return n+1
            return 0
        else:
            return 1
    else:
        return 1

print(find_missing_number(sequence))


#Cool solution
# def find_missing_number(sequence):
#     try:
#         numbers = sorted([int(x) for x in sequence.split()])
#         for i in range(1, len(numbers)+1):
#             if i not in numbers:
#                 return i
#     except ValueError:
#         return 1
#
#     return 0
