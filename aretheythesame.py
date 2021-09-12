"""
Are they the "same"?
If, for example, we change the first number to something else, comp may not return true anymore:
"""

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]

def comp(a, b):
    try:
        if len(a) == len(b):
            for i in a:
                if i**2 in b:
                    b.remove(i**2)
                    continue
                else:
                    return False
            return True
        return False
    except:
        return False

print(comp(a, b))
