import math

n = 0
# if str(math.sqrt(n)).split('.')[-1] == '0':
#     print('Yes')
# else:
#     print('No')

def is_square(n):
    return True if n >= 0 and str(math.sqrt(n)).split('.')[-1] == '0' else False
# print(True if str(math.sqrt(n)).split('.')[-1] == '0' else False)

print(is_square(n))

# Cool solution
def is_square(n):
  return n >= 0 and int(math.sqrt(n)) ** 2 == n
