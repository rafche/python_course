# dictionaries
# dictionaries eq. associative array

my_dog = {}
gps = {'Traker_id':'#454681'}

print(my_dog)

# adding key value pairs
my_dog['breed'] = 'Beagle'
my_dog['age'] = 5
my_dog['name'] = 'Lynx'

print(my_dog)

# accessing elements

print('The name of my dog is {}'.format(my_dog['name']))
print('{} is {} years old'.format(my_dog['name'], my_dog['age']))
print('---------\n')

# updating dictionary

my_old_dog = dict.copy(my_dog)
my_dog['breed'] = 'Collie'

print('{}'.format(my_dog['breed']))
print('---------\n')

# check for keys element exists in dict
# this is recommended to do before trying to access keys in dict
# because, when the key is not existing, it would crash the application

if 'name' in my_dog:
    print('there is a name in my_dog....{}'.format(my_dog['name']))
print('---------\n')


# merging dictionaries
# update can used to add new key value pairs, or merge other dicts,
# or overwrite existing key value pairs

my_dog_with_gps ={}
my_dog_with_gps.update(my_dog)
my_dog_with_gps.update(gps)

for value in my_dog_with_gps:
    print('key:',value, ' Value:', my_dog_with_gps[value])