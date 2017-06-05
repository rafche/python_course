# lists are powerful
# lists are mutable
# append and pop

some_list = []

print(some_list)

some_list.append('John')

print(some_list)

some_list.append('Connur')

print(some_list)

some_list.pop(-1)

print(some_list)

some_list.append('Connor')

print(some_list)

# iterating over lists

for element in some_list:
    print(element)

# lists can contain everything
# for examples tuples

print('\n\n---------------------')

another_list = ['a', 'b', 'c', ('inside', 'tuple')]

for element in another_list:
    print(element)

# or other lists
list_of_lists = []
sublist = [1, 2, 3]
sublist2 = ['red', 'blue', 'green']
sublist3 = [7, 8, 9]

list_of_lists.append(sublist)
list_of_lists.append(sublist2)
list_of_lists.append(sublist3)

for sub_list in list_of_lists:
    print(sub_list)
    print(type(sub_list))
print('\n\n---------------------')

# to get the value, we have to dig deeper

for sub_list in list_of_lists:
    for value in sub_list:
        print(value)


# lists are mutable
# that makes list very attractive for data manipulation


print(sublist)
sublist[0] = 'purple'
print(sublist)
sublist.clear()
print(sublist)
print('\n\n---------------------')

# accessing, manipulating elements in Lists

# fist element
print(sublist2[0])

# last element
print(sublist2[-1])

# deleting single value
del sublist2[1]
print(sublist2)

# check for elements in lists

print('red' in sublist2)

#

colors = ['red', 'blue', 'green', 'brown', 'purple', 'orange', 'pink', 'black']
print(colors)
print(sorted(colors))
# sorted doesnt affect the element, it is possible to  apply on a tuple
print(colors)
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)

# list comprehensions

# let's try some exercises
# ex_2_1 flat a list of lists to one list object
# ex_2_2 type in your name, check of how many different letters your name consist
# ex_2_6 showcase for mixed datatypes