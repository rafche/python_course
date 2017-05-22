
# declaration
pos_int = 3
pos_float = 3.14
fake_int = '3'
string_ = 'hello world'
neg_float = pos_float * -1


# print() --> Output Console
print(pos_int)
print(pos_float)
print(fake_int)
print('------------')


# abs() --> print only positive Numbst
print(neg_float)
print(abs(neg_float))


# print multiple Items
print(pos_int, pos_float, fake_int, string_)
print(pos_int, '-', pos_float, '-', fake_int + '-' + string_)
print('------------')

# print string & a number is not working with plus
# print(a + d)
# use instead comma
print(pos_int, pos_float)
print('------------')


# print() --> Output Console
print('------------')
print(type(pos_int))
print(type(pos_float))
print(type(fake_int))
print(type(string_))
print('------------')

# calculation in print statement is possible
print('------------')
print(pos_int + pos_float + pos_int * pos_float)
print(pos_int * pos_int)
print(pos_int / pos_float)
print('------------')

#Strings are powerful
aString = 'nobody expects the spanish inquisition'
print(aString)
print(len(aString))

# Strings can be shorted by stop and start Position
# where xx: marking the beginning Position and :xx marking the end Position
print(aString[:-11])
print(aString[:11])
print(aString[-6:])
print(aString[6:])

# sometimes you only need a part of a Sting
# split() can be the Solution
# the result of a split is a list

sentence = 'is honduras the same as belize'
word = sentence.split(' ')
print(word)

print('------ Casting to diff. Formats ------')

#print(b - c) // Type Error

# casting to datatype int, float, string
print(pos_float - int(fake_int))
print()
print(type(pos_int))
print(type(str(pos_int)))








