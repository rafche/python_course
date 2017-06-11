"""
--> first and second name, <-- longer name
"""

first_name = input('please type in your first name \n')
second_name = input('please type in your second name \n')

if len(first_name) > len(second_name):
    print('your first name is longer than your second name')
elif len(first_name) < len(second_name):
    print('your second name is longer than your first name')
else:
    print('your first and second name have the same amount of characters')
