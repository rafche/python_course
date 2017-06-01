import collections

info_person = collections.namedtuple('person', 'first_name, second_name, age, sex')


person_1 = info_person('Sarah','Parker', 40, 'f')

print(person_1)

print('My name is {}'.format(person_1.first_name))

