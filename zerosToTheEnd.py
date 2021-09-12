"""
Moving Zeros To The End
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""

array = []
def move_zeros(array):
    for x in array:
        if x == 0:
            array.remove(x)
            array.append(x)
    return array

# print(move_zeros(array))
for x in (array.remove(x).append(x) for x in array  if x == 0):
    print(x)
