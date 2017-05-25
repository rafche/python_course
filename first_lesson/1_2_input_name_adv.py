"""
--> nothing, <-- greeting random name
User types in Name, getting greet
"""
# if the module is not known by Pycharm, a red exclamation appears
import faker

for i in range(0, 10):
    print('hello {}'.format(faker.Factory.create().name()))
    print(i)


# it is also possible to other way around
my_factory = faker.Factory.create()

# my_factory is a Generator object
# which means it is iteratable from outside the Object / function
print(type(my_factory))

for i in range(10):
    print('hello {}'.format(my_factory.name()))




