# x, y, bin, result
# ...x...x...x...x
# printing

import random



for i in range(100):
    y = random.randrange(100)
    x = random.randrange(100)
    bin = random.randrange(7)
    result = random.randrange(2)
    print('{:4d}{:4d}{:4d}{:4d}'.format(x, y, bin, result))