"""
--> input number, <-- true / false
it is a simple guessing the number  game
"""

secret_number = 42

usernumber = int(input('please guess the secret number,(0 - 99)\n'))

while not usernumber == secret_number:

    if usernumber < secret_number:
        print('your guessed number is too low')
    elif usernumber > secret_number:
        print('your guessed number is too high')

    usernumber = int(input('please give it another try\n'))

else:
    print(f'you guessed the secret number, {secret_number}')
