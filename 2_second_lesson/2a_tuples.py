# tuples are immutable
# the content of a tuple can be everything (numbers, strings, tuples, )
# once build, can't be modified


tuple_1 = (1, 2, 3, 4)
tuple_2 = ('hello', 'python', 4, 5)

# you can iterate over a tuple

for element in tuple_1:
    print(element)

# display index
# tuples are zero-based

for i, element in enumerate(tuple_2):
    print(i, ' ', element)

# you can also print tuple by index like this

print(tuple_2[1])

# but this is very very dangerous!
# when you try to access a non existing element, it will wreck up your application
# following Error will be shown
# IndexError: tuple index out of range

#print(tuple_2[200])

# len() can applied to tuple

print('len of tuple_1 = {}'.format(len(tuple_1)))


# tuples can also contain other tuples

tuple_3 = (1,2,3,(2,34.5,'ab'),(1,2,3))

print('len of tuple_3 = {}'.format(len(tuple_1)))


for element in tuple_3:
    print(element, ' -- the type is {}'.format(type(element)))

# packing tuples
diex = 8
diey = 12

coord = (diex, diey)


# unpacking tuples,

tuple_4 = ('Time Bandit', 6, 34)

ship, crew, length = tuple_4

print(ship, crew, length)

# this code will break if there are more values as expected

# ship, crew = tuple_4

# just add _ for ignoring the following values

ship, crew, _ = tuple_4

print(f'{ship} {crew}')

