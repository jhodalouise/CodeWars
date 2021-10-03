'''
6 kyu Who likes it?

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
'''
names = ["Peter"]

# if len(names) == 1:
#     print(names[0], 'likes this')
# elif len(names) == 2:
#     print(' and '.join(names), 'like this')
# elif len(names) == 3:
#     print('{}, {} and {} like this'.format(names[0],names[1],names[2]))
# elif len(names) > 3:
#     print('{}, {} and '.format(names[0],names[1]) + str(len(names[2:]))  + ' others like this')
# else:
#     print('no one likes this')

def likes(names):
    if len(names) == 1:
        return names[0] + ' likes this'
    elif len(names) == 2:
        return ' and '.join(names) + ' like this'
    elif len(names) == 3:
        return '{}, {} and {} like this'.format(names[0],names[1],names[2])
    elif len(names) > 3:
        return '{}, {} and '.format(names[0],names[1]) + str(len(names[2:]))  + ' others like this'
    else:
        return 'no one likes this'

print(likes(names))
