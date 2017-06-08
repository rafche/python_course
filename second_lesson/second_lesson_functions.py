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

# you can call a function in a function, it's also possible to call the same function

print(add(add(5, 5), c))

o = add(5, o)

print(o)


# a function doesn't need an input or a return value

def hello():
    '''
    :return: print hello world 
    '''
    print('hello World')


hello()


# it is important to pass parameters in the same order as defined

def division(a, b):
    return a / b


print(division(15, 5))

# there is a way to pass in different order, by using Keywords

print(division(5, 15))

print(division(b=5, a=15))

# it is also possible to put a function in a function

def stringrev(simple_string):
    '''
    --> String, <-- reversed upper and lower Case String
    :param simple_string: input String 
    :return: reversed String
    '''
    def reverse_case(letter):
        if letter.islower() == True:
            return letter.upper()
        else:
            return letter.lower()
    '''
    --> letter, <-- letter upper and lower case reversed 
    '''
    reversed_String = ''
    for letter in simple_string:
        temp_letter = reverse_case(letter)
        reversed_String += temp_letter
    return reversed_String

print(stringrev('Why eleven is NOT called onety one'))

# python also let you describe your input type,
# this is very helpful for the linting

def lower_name(input_name : str):
    return input_name.lower()



# let's try some exercises
# ex_2_4 write a function that takes 2 parameter (number) and return the higher number, or False if the numbers equal
# ex_2_5 write a 'calculator' function, takes 2 numbers and one arithmetic Operator
