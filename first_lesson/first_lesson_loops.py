# loops
# there a two different loops in python
# for and while

word = 'Tohuwabohu'
sentence = 'Lorem ipsum dolor sit amet...'

# ----------- for loop -----------
# looping from 0 to 9

for i in range(10):
    print(i)

print('\n\n-----------\n\n')


# looping from 5 to 9

for i in range(5, 10):
    print(i)

print('\n\n-----------\n\n')


# looping from 0 to 98, take every second number
# the third arg is the step width

for i in range(0, 100, 2):
    print(i)
    if i >= 10:
        print('i is greater than{}'.format(10))
        break

print('\n\n-----------\n\n')


# leave the loop by condition

for i in range(0, 100):
    print(i)

print('\n\n-----------\n\n')


# strings as an iterable
# this will print every letter of 'word'
for letter in word:
    print(letter)

print('\n\n-----------\n\n')

# you can also print the index

for i, letter in enumerate(word):
    print(letter + ' has index of ', i)

print('\n\n-----------\n\n')


# lets do it in reverse

for letter in reversed(word):
    print(letter)

print('\n\n-----------\n\n')


# iterating over a sentence

for word in sentence.split():
    print(word)

print('\n\n-----------\n\n')
print('\n\n-----------\n\n')

# print the word in a sentence reversed

for word in sentence.split():
    temp = ''
    for letter in reversed(word):
        temp += letter
    print(temp)

print('\n\n-----------\n\n')


# continue Statement can be used to jump over

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

x = 0
while x < 10:
    print(x)
    x += 1

print('\n\n-----------\n\n')


# can also apply to truthiness of objects

w = ['one', 'two', 'three', 'four', 'five']

while w:
    print(w)
    w.pop(0)

print('\n\n-----------\n\n')

