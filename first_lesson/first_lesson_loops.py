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


# let's try some exercises
# ex_1_7


