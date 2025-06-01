while True:
    print('please type your name.')
    name = input ()
    if name == 'Carlos':
        break # exits the loop if the name is Carlos
    else:
        print('Please try again, ' + name + '.')
        continue
print('Thank you' +  name )