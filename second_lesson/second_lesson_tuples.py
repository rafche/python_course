# tuples are immutable
# the content of a tuple can be everything (numbers, strings, tuples, )
# once build, can't be modified

tuple_1 = (1, 2, 3, 4)
tuple_2 = ('hello', 'python', 4, 5)
# you can iterate over a tuple

for element in tuple_1:
    print(element)

# lets display index
# tuples are zerobased

for i, element in enumerate(tuple_2):
    print(i,' ', element)

# you can also print tuple by index like this

print(tuple_2[1])

# but this is very very dangerous!
# when you try to access a non existing element, it will wreck up your application
# following Error will be shown
# IndexError: tuple index out of range

#print(tuple_2[200])

