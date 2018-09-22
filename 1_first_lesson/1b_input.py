"""
let's try some ineractive application
"""

first_number = input('please enter a number between 1 and 100\n')
second_number = input('please enter a number between 1 and 100\n')



try:
    a = first_number + second_number
    print(first_number + second_number)
except Exception as e:
    print("user input is always a dangerous thing!")


# what a guessing?
# todo: insert a guessing.
# python is guessing wrong,
# give it a second try

try:
    print(int(first_number) + int(second_number))
except Exception as e:
    print("user input is always a dangerous thing!")

def insertTwoNumbers():
    # also a possible way casting the input to a data type
    # in my opinion the better & beautifuler way

        first_number = int(input('please enter a integer between 1 and 100\n'))
        second_number = int(input('please enter a integer between 1 and 100\n'))

        print(first_number + second_number)


if __name__ == "__main__":
    try:
        insertTwoNumbers()
    except Exception as e:
        print("the error is handed up through layers!")
