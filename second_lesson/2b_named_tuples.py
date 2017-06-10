import collections

# named tuples are very useful for passing data to functions,....


person_info = collections.namedtuple('person', 'first_name, second_name, age, sex')

person_1 = person_info('Sarah', 'Parker', 40, 'f')

print(person_1)

print('My name is {}'.format(person_1.first_name))

