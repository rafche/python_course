# organize code in functions is more efficient
# you can call a function only after the declaration

def add(a, b):
    '''
    :takes two parms, building sum
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



