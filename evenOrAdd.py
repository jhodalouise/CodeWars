'''
8 kyu - Even or Odd
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
'''

number = 1545452

def even_or_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'

print(even_or_odd(number))
