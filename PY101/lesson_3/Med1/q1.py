def add_dash(string):
    counter = 0
    dash = '-'
    while counter < 10:
        string = dash + string
        print(string)
        counter += 1

quote = 'The Flintstones Rock!'
add_dash(quote)


for padding in range (1,11):
    print(f'{'-' * padding}The Flintstones Rock!')