'''
6 kyu - Format a string of names like 'Bart, Lisa & Maggie'.
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
'''

names = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]

def namelist(names):
    if len(names) == 1:
        return names[0]['name']
    elif len(names) == 0:
        return ''
    else:
        return ', '.join([name['name'] for name in names[:-1]]) + ' & ' + names[-1]['name']

print(namelist(names))
