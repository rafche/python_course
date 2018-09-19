# use the escaping pattern
# https://docs.python.org/2.0/ref/strings.html

# printing a Backslash
print('\\')

print('\n')
# printing quotes
print('I\'m hungry')

# print a path
print('{:-^30}'.format('look at the difference'))
print('C:\\temp\\python\\no\\one\\expects\\the\\Spanish\\Inquisition')
print("""C:\\temp\\python\\no\\one\\expects\\the\\Spanish\\Inquisition""")

# printing newlines
print('\n{:-^30}'.format('the power of editing text'))
print('hi \n'
      ' there')

# dealing with print statements over several lines

# using triple quotes, includes the line breaks
print('\n{:-^30}'.format('block with triple quotes'))
print("""
3F9F636B5A
6B9D47EC9D
3A18EBB29E
F7267EC8EE
6E08682AEE
ED46C0129F
FFABF388ED
E7034A7D12
30ADEE7C24
7D046E29BF
448B15E666
123BA2A839
BC41017354""")


# for triple quoting .format or f string works
print('\n{:-^30}'.format('block with .format'))
print("""3F9F636B5A
6B9D47EC9D
3A18EBB29E
F7267EC8EE
6E08682AEE
ED46C0129F
FFABF388ED
E7034A7D12
30ADEE7C24
7D046E29BF
{:_^10}
123BA2A839
BC41017354""".format('ADEE7N'))



print('\n{:-^30}'.format('block with f string'))
location = '##########'

print(f"""3A18EBB29E
F7267EC8EE
{location}
ED46C0129F
FFABF388ED
E7034A7D12""")

print('\n{:-^30}'.format('single quotes'))

# using single quotes
print('6B9D47EC9D\n'
'3A18EBB29E\n'
'F7267EC8EE\n'
'6E08682AEE\n'
'ED46C0129F\n'
'FFABF388ED\n'
'E7034A7D12\n'
'30ADEE7C24\n'
'7D046E29BF\n')

print('\n{:-^30}'.format('block with text formating'))
print('{:-^200}'.format(
'\n6B9D47EC9D\n'
'3A18EBB29E\n'
'F7267EC8EE\n'
'6E08682AEE\n'
'ED46C0129F\n'
'FFABF388ED\n'
'E7034A7D12\n'
'30ADEE7C24\n'
'7D046E29BF\n'))