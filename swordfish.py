while True: 
    print('Please type in your name')
    name = input ()   # name declared as input 
    if name != 'joe': # if the name is not (!=) joe, the program will continue to loop
        continue # sends the user back to the beginning of the loop if the name is not joe
    while True: # creates a nested loop, another loop inside the first loop
        print('hello, joe. what is the password?' 'it is a fish.') # if name is joe, program will print this line
        password = input ()
        if password != 'swordfish':
            print('incorrect, please try again') 
            continue #sends user to nested loop to re-enter password 
        else: # clause for the else statement, if the password is correct
            print('access granted')
            break