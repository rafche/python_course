# dictionaries
# dictionaries eq. associative array
#

my_dog = {}
gps = {'Traker_id':'#454681'}

print(my_dog)

my_dog['breed'] = 'Beagle'
my_dog['age'] = 5
my_dog['name'] = 'Lynx'

print(my_dog)

# accessing elements

print('The name of my dog is {}'.format(my_dog['name']))
print('{} is {} years old'.format(my_dog['name'], my_dog['age']))


# merging dictionaries

my_dog_with_gps ={}
my_dog_with_gps.update(my_dog)
my_dog_with_gps.update(gps)

for value in my_dog_with_gps:
    print('key:',value, ' Value:', my_dog_with_gps[value])

