'''
6 kyu - Replace With Alphabet Position

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
Example

alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
'''
import string


def alphabet_position(text):
    alphabets = string.ascii_lowercase
    letter_position = dict()

    counter = 1
    for alphabet in alphabets:
        letter_position[alphabet] = counter
        counter += 1

    return ' '.join([str(letter_position[char.lower()]) for char in text if char.isalpha()])


tests = ["The sunset sets at twelve o' clock.","The narwhal bacons at midnight."]

for text in tests:
    result = alphabet_position(text)
    print(text,':',result)
