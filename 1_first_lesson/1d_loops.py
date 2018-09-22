# loops
# there a two different loops in python
# for and while

word = 'Tohuwabohu'
sentence = 'Lorem ipsum dolor sit amet...'

# ----------- for loop -----------
# numeric loops are different in python
# range is technically seen a object(generator), that returns a sequence of numbers
# bee careful in python 2 range returns a list with every number, use instead xrange

def printRangeandType():
    print(range(1,20))
    print("Type of \'range(1,20)\' =",  type(range(1,20)))


def forLoopwithRange():
    print('\n\n-----------\n\n')

    # looping from 0 to 9
    for i in range(10):
        print(i)

    print('\n\n-----------\n\n')

def forLoopwithdefinedRange():
    # looping from 5 to 9
    print('\n\n-----------\n\n')

    for i in range(5, 10):
        print(i)

    print('\n\n-----------\n\n')


def forLoopwithStepRange():
    # looping from 0 to 99, take every second number
    # the third arg is the step width
    print('\n\n-----------\n\n')

    for i in range(0, 100, 2):
        print(i)
        if i >= 10:
            print('i is greater than {}'.format(10))
            break

        print('\n\n-----------\n\n')


def forLoopwithBreak():
    # leave the loop by condition
    print('\n\n-----------\n\n')

    for i in range(0, 100):
        print(i)
        if i == 50:
            break

    print('\n\n-----------\n\n')


def forLoopwithaString():
    # strings as an iterable
    # this will print every letter of 'word'
    print('\n\n-----------\n\n')

    print("LoopString: ", word)
    for letter in word:
        print(letter)

    print('\n\n-----------\n\n')


def forLoopwithEnumerate():
    # you can also print the index
    # the return value is a tuple with the value and index
    print('\n\n-----------\n\n')

    for letter in enumerate(word):
        print(letter)

    print('\n\n-----------\n\n')


def unpacktheTuble():
    # tuples can be easily unpack
    print('\n\n-----------\n\n')

    for i, letter in enumerate(word):
        print(letter + ' has index of ', i)

    print('\n\n-----------\n\n')


def readReverse():
    # lets do it in reverse
    print('\n\n-----------\n\n')

    for letter in reversed(word):
        print(letter)

    print('\n\n-----------\n\n')

def forLoopwithSplit():
    # iterating over a sentence

    print('\n\n-----------\n\n')

    for word in sentence.split():
        print(word)

    print('\n\n-----------\n\n')

def forLoopwithSplitReverse():
    # print the word in a sentence reversed
    print('\n\n-----------\n\n')

    for word in sentence.split():
        temp = ''
        for letter in reversed(word):
            temp += letter
        print(temp)

    print('\n\n-----------\n\n')

def forLoopwithContine():
    # continue Statement can be used to jump over
    print('\n\n-----------\n\n')

    for letter in 'pythonic':
        if letter == 'o':
            continue
        print(letter)

    print('\n\n-----------\n\n')


# let's try some exercises
# ex_1_7 find the longest sequence of increasing letters in a String


# ----------- while loop -----------
# the loop is running until the statement is False
# python doesn't support x++
# be careful to don't produce an infinite loop
def whileLoop():
    print('\n\n-----------\n\n')

    x = 0
    while x < 10:
        print(x)
        x += 1

    print('\n\n-----------\n\n')

def whileLoopoverStrings():
    # can also apply to truthiness of objects
    print('\n\n-----------\n\n')

    w = ['one', 'two', 'three'
        , 'four', 'five']

    while w:
        print(w)
        w.pop(0)

    print('\n\n-----------\n\n')

if __name__ == "__main__":
    printRangeandType()
    forLoopwithRange()
    forLoopwithdefinedRange()
    forLoopwithStepRange()
    forLoopwithBreak()
    forLoopwithaString()
    forLoopwithEnumerate()
    unpacktheTuble()
    readReverse()
    forLoopwithSplit()
    forLoopwithSplitReverse()
    forLoopwithContine()
    whileLoop()
    whileLoopoverStrings()