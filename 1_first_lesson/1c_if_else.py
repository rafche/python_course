# conditional statement
# if else elif

pos_int = 16
limit = 16

def greaterThen():
    # if needs always statement which is true or false
    # if else statement don't need the else statement
    if pos_int > limit:
        print('{} is greater than {}'.format(pos_int, limit))

def globalgreaterThenTwoArguments(a,b):
    # if needs always statement which is true or false
    # if else statement don't need the else statement
    if a > b:
        print('{} is greater than {}'.format(pos_int, limit))
def localgreaterThenTwoArguments(a,b):
    # if needs always statement which is true or false
    # if else statement don't need the else statement
    if a > b:
        print('{} is greater than {}'.format(a, b))

def elseStatement():
    # if else with else statement
    if pos_int < limit:
        print('{} is less than {}'.format(pos_int, limit))
    else:
        print('{} is greater than {}'.format(pos_int, limit))

def elifStatement():
    # if else elif
    # with the elif statement, more checks are possible
    if pos_int < limit:
        print('{} is less than {}'.format(pos_int, limit))
    elif pos_int > limit:
        print('{} is greater than {}'.format(pos_int, limit))
    else:
        print('{} is equal than {}'.format(pos_int, limit))


def longVersion():
    # also possible, but longer syntax
    if pos_int < limit:
        print('{} is less than {}'.format(pos_int, limit))
    else:
        if pos_int > limit:
            print('{} is greater than {}'.format(pos_int, limit))
        else:
            print('{} is equal to {}'.format(pos_int, limit))


def andCondition():
    # combine conditions with 'and' or 'or'
    # Python doesn't support && or ||
    if not pos_int < limit and not pos_int > limit:
        print('{} is equal to {}'.format(pos_int, limit))

def orCondition():
    if pos_int < limit or pos_int > limit:
        print('{} is NOT equal to {}'.format(pos_int, limit))


def typeBoolean():
    # i use the chance to introduce a new type: boolean
    # the Bool can be True or False

    ex_bool = pos_int > limit
    print(ex_bool)
    print(type(ex_bool))

if __name__ == "__main__":
    greaterThen()
    elseStatement()
    elseStatement()
    longVersion()
    andCondition()
    orCondition()
    typeBoolean()
    globalgreaterThenTwoArguments(7, 3)
    localgreaterThenTwoArguments(7, 3)
# Let's do some exercises
# ex1_5 type in your full name, an check which name is longer
