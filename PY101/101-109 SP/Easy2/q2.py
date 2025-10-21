#get user name from input
#greet user with input name
#if ends with "!", print greeting in uppercase

name = input('What is your name? ')

if name.endswith('!'):
    print(f'HELLO {name.upper()} WHY ARE WE YELLING')
else:
    print(f'Hello {name}')
