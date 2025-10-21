number = int(input('Please enter an integer greater than 0: '))
operation = input('Enter "s" to compute the sum, or "p" to compute the product: ')

if operation == 's':
    print(sum(range(1, number + 1)))
  
elif operation == 'p':
    product = 1
    for integer in range(1,number+1):
        product *= integer
    print(product)

else:
    print('Oops. Unknown operation')
    