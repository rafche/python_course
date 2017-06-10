# dictionaries
# dictionaries eq. associative array
#

my_dog = {}

print(my_dog)

my_dog['breed'] = 'Beagle'
my_dog['age'] = 5
my_dog['name'] = 'Lynx'

print(my_dog)

# accessing elements

print('The name of my dog is {}'.format(my_dog['name']))
print('{} is {} years old'.format(my_dog['name'], my_dog['age']))

# adding Tuples to dict

my_dog['childs']= ['Roofus','Cassiopeia']