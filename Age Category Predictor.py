print('Age Category Checker')
age = (input('Enter your age:')) # Prompt user for their age
age = int(age)     # Convert input to integer, it declares that the the requested input above is to be acknowledged as an integer
if age < 5:
    print('You are a toddler.')     # If the age is less than 5, print that the user is a toddler
elif age < 13:
    print('You are a child.')        # If the age is less than 13, print that the user is a child      
elif age < 20:
    print('You are a teenager.')     # If the age is less than 20, print that the user is a teenager   
elif age < 65:
    print('You are an adult.')       # If the age is less than 65, print that the user is an adult
else:
    print('You are a senior citizen.')
# If the age is 65 or older, print that the user is a senior citizen
print('Thank you for using the Age Category Checker!')  # Print a thank you message
SystemExit # Exit the program
# The program ends here, and the user is informed that the program has ended.  
