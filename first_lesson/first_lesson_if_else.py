# conditional statement
# if else elif

pos_int = 16
limit = 15

# if needs always statement which is true or false
# if else statement don't need the else statement
if pos_int > limit:
    print('{} is greater than {}'.format(pos_int, limit))


# if else with else statement
if pos_int < limit:
    print('{} is less than {}'.format(pos_int, limit))
else:
    print('{} is greater than {}'.format(pos_int, limit))


# if else elif
# with the elif statement, more checks are possible
if pos_int < limit:
    print('{} is less than {}'.format(pos_int, limit))
elif pos_int > limit:
    print('{} is greater than {}'.format(pos_int, limit))
else:
    print('{} is equal than {}'.format(pos_int, limit))


# also possible, but longer syntax
if pos_int < limit:
    print('{} is less than {}'.format(pos_int, limit))
else:
    if pos_int > limit:
        print('{} is greater than {}'.format(pos_int, limit))
    else:
        print('{} is equal than {}'.format(pos_int, limit))


# i use the chance to introduce a new type boolean
# the Bool can be True or False

ex_bool = pos_int > limit
print(ex_bool)
print(type(ex_bool))



# Let's do some excersices
# ex1_6 type in your full name, an check which name is longer