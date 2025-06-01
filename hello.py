# This program says hello and asks for my name.

print('Hello world!')
print('What is your name?') # ask for their name
myName = input()
print ('It is good to meet you,' + myName)
print ('The length of your name is:')
print(len(myName)) #len() function counts the number of characters in a string
print ('What is your age?') #ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
