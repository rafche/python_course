"""
User input should be like 
first Number
arithmetic Operator
second Number

Return value should be the result of the arithmetic Operation
"""

def calculator(a, operator, b):
    '''
    :param a: first Number 
    :param operator: arithmetic Operator
    :param b: second Number
    :return: 
    '''
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return 'operator unkown'

first_number = float(input('please enter your fist number\n'))
operator = str(input('please enter your Operator\n'))
second_number = float(input('please enter your second number\n'))

print(calculator(first_number, operator, second_number))
