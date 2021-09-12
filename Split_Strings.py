"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

"""

s = 'abcdef'
def solution(s):
    result = list()
    before = 0
    c = 2
    if len(s) % 2 != 0:
        length = int(len(s)/2) + 1
    else:
        length = int(len(s)/2)
    for i in range(length):
        if list(s)[i]:
            elem = ''.join(s[before:c])
            if len(elem) == 2:
                result.append(elem)
                before = c
                c += 2
            else:
                result.append(s[-1]+'_')
    return result


# Cool solution
# def solution(s):
#     result = []
#     if len(s) % 2:
#         s += '_'
#     for i in range(0, len(s), 2):
#         result.append(s[i:i+2])
#     return result
