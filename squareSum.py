'''
8 kyu Square(n) Sum
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
'''
numbers = [-1,0,1]

def square_sum(numbers):
    return sum(map(lambda x: x**2,numbers))

print(square_sum(numbers))
