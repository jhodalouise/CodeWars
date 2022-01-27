'''
7 kyu - Mumbling
This time no story, no theory. The examples below show you how to write function accum:
Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''
s = "cwAt"

def accum(s):
    return '-'.join((j * i).title() for i,j in enumerate(s,1))

print(accum(s))
