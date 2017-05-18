'''
iterating over String
'''

str_name = 'Philipp'

# iterating over string
for letter in str_name:
    print(letter)

# iterating over string and displaying index
for i, letter in enumerate(str_name):
    print(letter, i)

# iterating over sting in reverse
for letter in reversed(str_name):
    print(letter)
