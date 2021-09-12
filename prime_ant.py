"""
Prime ant
The Prime ant (A293689) is an obstinate animal that navigates the integers and divides them until there are only primes left, according to the following procedure:

    An infinite array/list A is initialized to contain all the integers greater than 1: [2, 3, 4, 5, 6, …]
    Let p be the position of the ant on the array/list. Initially p = 0, so the ant is at A[0] = 2
    At each turn, the ant moves as follows:
        If A[p] is prime, move the ant one position forward, so p ← p + 1
        Otherwise (if A[p] is composite):
            Let q be its smallest divisor greater than 1
            Replace A[p] with A[p] / q
            Replace A[p−1] with A[p−1] + q
            Move the ant one position backward, so p ← p − 1

Your task is to comlete the function that computes the position of the prime ant after n turns.
Examples

prime_ant(2)   # => 2
prime_ant(11)  # => 5
prime_ant(47)  # => 9
"""

import itertools

A = [i for i in itertools.count(start = 2)]

# A = [2, 3, 4, 5, 6, 7]
#
p = 0
n = 11
turn = 0
for a in A:
    if a == 2 or a == 3:
        p += 1
        turn += 1
    elif A[p] % 2 == 0:
        A[p] = A[p] / 2
        p -= 1
        turn += 1
    elif A[p] % 3 == 0:
        A[p] = A[p] / 2
        p -= 1
        turn += 1
    else:
        p += 1
        turn += 1

    if n == turn:
        print(p)
