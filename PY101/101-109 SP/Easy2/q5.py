#prompt user for a number - will be a float
#prompt user for another number - will be a float
#print addition of number
#print sub of numbers
#print product
#print quotient
#print floor qoutient
#print remainer
#print power

def prompt(string):
    print(f'==> {string}')

prompt('Enter the first number: ')
number1 = float(input())

prompt('Enter the second number: ')
number2 = float(input())

prompt(f'{number1} + {number2} = {number1 + number2}')
prompt(f'{number1} - {number2} = {number1 - number2}')
prompt(f'{number1} * {number2} = {number1 * number2}')
prompt(f'{number1} / {number2} = {number1 / number2}')
prompt(f'{number1} // {number2} = {number1 // number2}')
prompt(f'{number1} % {number2} = {number1 % number2}')
prompt(f'{number1} ** {number2} = {number1 ** number2}')