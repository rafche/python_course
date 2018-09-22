def hardtrap():
    # trapped in while loop till user_input == expected_input:

    expected_input = 'x'
    user_input = ''

    while user_input != expected_input:
        user_input = input('press [x]')
    else:
        print('good bye')

def easytrap():
    # trapped in while loop till user_input == expected_input:
    expected_input = ['x','end','exit','letmego','leave']
    user_input = ''
    exit = True

    while exit:
        user_input = input('insert [help]')
        for exitcode in expected_input:
            if user_input == exitcode:
                exit = False
            elif user_input == 'help':
                print("insert one of the following to end it!")
                for exitcode in expected_input:
                    print(exitcode)
                #do not loop over both loops
                #break only break one loop
                break
    else:
        print('good bye')


if __name__ == "__main__":
    easytrap()
    #hardtrap()
