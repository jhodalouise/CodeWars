'''
7 kyu Sum of odd numbers
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...

Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
'''
def row_sum_odd_numbers(n):
    return n ** 3

# My original solution before I realized that solution was hella eazzzzy -.-
def row_sum_odd_numbers_solution2(n):
    odds = list()
    counter = 1
    if n > 1:
        for i in range(1,n**2):
            if i == 1:
                odds.append(i)
            else:
                odds.append(i+counter)
                counter += 1
        start = odds.index(((n-1)*n)+1)
        return sum(odds[start:start+n])
    else:
        return 1

tests = [1,2,13,19,41]

for test in tests:
    result = row_sum_odd_numbers(test)
    print(test,result)
