# organize code in functions is more efficient
# you can call a function only after the declaration
o = 20


def add(a, b):
    '''
    takes two params, building sum
    :param a: first addend 
    :param b: second addend
    :return: sum of a,b
    '''
    return a + b


add(2, 5)

# print(a), this will not work, because a and b only known by the function
# let's print the return value

print(add(4, 5))

# or fill a variable

c = add(5, 6)

# you can call a function in a function, it'S also possible to call the same function

print(add(add(5, 5), c))

o = add(5, o)

print(o)


# let's try some exercises
# ex_2_4 write a function that takes 2 parameter (number) and return the higher number, or False if the numbers equal
# ex_2_5 write a 'calculator' function, takes 2 numbers and one arithmetic Operator
