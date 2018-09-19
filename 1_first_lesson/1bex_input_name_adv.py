"""
--> nothing, <-- greeting random name
User types in Name, getting greet
"""
# if the module is not known by Pycharm, a red exclamation appears
import faker

def onehundredFakeNames():
    for i in range(0, 100):
        print('hello {}'.format(faker.Factory.create().name()))
        # print(i)

def tenFakeNames():
    # another way
    my_factory = faker.Factory.create()

    for i in range(10):
        print('hello {}'.format(my_factory.name()))

def typeOfFaker():
    my_factory = faker.Factory.create()
    print(type(my_factory))
    # my_factory is a Generator object
    # which means it is iterable from outside the Object / function

if __name__ == "__main__":
    onehundredFakeNames()
    tenFakeNames()
    typeOfFaker()
