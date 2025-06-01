print('what is the secret number?')
secret_number = int(7) #declaring secret number a variable worth the value of 7
input('please guess the secret number: ') # prompts user to guess 

while input != int(7): 
    print('incorrect, try again')
    input('Would you like a clue? (y/n)') # prompts user to ask for a clue
    while True:
        clue = input()
        if clue == 'y':
            print('My favorite number')
            print('Please guess again: ')
            secret_number = int(input())
        elif clue == 'n':
            print('Please guess again: ')
            secret_number = int(input())
        else:
            print('Invalid input, please enter y or n.')
            continue
else:
    print('Congratulations! You guessed the secret number: ' + str(secret_number)) 

    # faulty code, for re-evaluation tomorrow 
    