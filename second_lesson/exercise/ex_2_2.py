"""
--> first and second name, <-- sum of different letters
"""
list_of_letters = []

first_name = input('please type in your first name \n')
second_name = input('please type in your second name \n')

for letter in first_name:
    if letter not in list_of_letters:
        list_of_letters.append(letter)

for letter in second_name:
    print(letter)
    if letter not in list_of_letters:
        list_of_letters.append(letter)

print(list_of_letters)