"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
"""

num = 0
def expanded_form(num):
    answer = []
    while num > 0:
        length = len(str(num)) - 1
        number_of_zeroes = ['0'] * length
        zeroes = ''.join(number_of_zeroes)
        subtrahend = str(num)[0] + zeroes
        answer.append(subtrahend)
        num = num - int(subtrahend)

    result = ' + '.join(answer)
    return result

print(expanded_form(num))
