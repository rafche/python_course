"""
--> two numbers, <-- highest number
return the highest number
"""


def multi(a, b):
    '''
    :param a: first number 
    :param b: second number
    :return: higher number
    '''
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return False


print(multi(15, 15))
