num = 0

# result = []
# for n in str(num):
#     n = int(n) ** 2
#     result.append(str(n))
#     final = ''.join(result)
# # print(final)
#
# print(int(''.join([str(int(n)**2) for n in str(num)])))

def square_digits(num):
    return int(''.join([str(int(n)**2) for n in str(num)]))

print(square_digits(9119))
