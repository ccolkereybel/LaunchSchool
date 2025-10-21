try:
    with open('example.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('The file does not exist')

