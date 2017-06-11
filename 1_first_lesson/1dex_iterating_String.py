'''
iterating over String
'''

str_name = 'Honduras'

# iterating over string
for letter in str_name:
    print(letter)
print('\n--------------\n')

# iterating over string and displaying index
for i, letter in enumerate(str_name):
    print(letter, i)
print('\n--------------\n')

# iterating over sting in reverse
for letter in reversed(str_name):
    print(letter)
print('\n--------------\n')

# it doesn't matter, which name you give the iterator
# in string context, it will be always iterating over the chars of the String
for whatever in str_name:
    print(whatever)