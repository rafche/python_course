"""
let's try some ineractive application
"""

first_number = input('please enter a number between 1 and 100\n')
second_number = input('please enter a number between 1 and 100\n')

print(first_number + second_number)

# python is guessing wrong,
# give it a second try

print(int(first_number) + int(second_number))

# also a possiple way casting the input to a data type
# in my opinion the better & beautifuler way

first_number = int(input('please enter a integer between 1 and 100\n'))
second_number = int(input('please enter a integer between 1 and 100\n'))

print(first_number + second_number)



