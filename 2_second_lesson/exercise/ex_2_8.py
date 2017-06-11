"""
hangman the game
"""
from randomwordgenerator import randomwordgenerator


def init():
    '''
    :return: random word
    '''
    return randomwordgenerator.generate_random_words(n=1).lower()


def masked_word(secret_word: str, letters_guessed: list):
    mask = ''
    for letter in secret_word:
        if letter in letters_guessed:
            mask += letter
        else:
            mask += '-'
    return mask


def available_letters(letters_guessed):
    '''
    :param letters_guessed: list of guessed letters 
    :return: available letters
    '''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    diff = []
    diff_formated = ''

    for letter in alphabet:
        if letter in letters_guessed:
            diff.append('_')
        else:
            diff.append(letter)

    for idx, element in enumerate(diff):
        if (idx + 1) % 5 == 0:
            diff_formated += element + ' ' + '\n'
        else:
            diff_formated += element + ' '

    return diff_formated


def check_word_guessed(secret_word, letters_guessed):
    '''
    :param secret_word:
    :param letters_guessed:
    :return: true for all letters
    '''
    for letter in secret_word:
        if letter in letters_guessed:
            pass
        else:
            return False
    return True


if __name__ == '__main__':

    while (1):
        guesses = 0
        t_limit = 5
        known_letters = []
        word_guessed = False

        print('Hi there, do you wanna play hangman?')
        command = input('[p]lay or [l]eave\n')

        if command == 'p':
            secret_word = init()
            while guesses < t_limit:
                print('\n\n' + masked_word(secret_word, known_letters))

                print(available_letters(known_letters))
                input_letter = input('\n guess a letter\n')

                if input_letter in known_letters:
                    print('letter already guessed')
                else:
                    known_letters.append(input_letter)

                if check_word_guessed(secret_word, known_letters):
                    print(secret_word)
                    print('yippie, you won')
                    break

                if input_letter not in secret_word:
                    guesses += 1
            else:
                print('you lost,')
                print(secret_word + '\n\n')

        elif command == 'l':
            break
        else:
            print('command not valid')