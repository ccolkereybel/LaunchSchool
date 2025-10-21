#write function that takes number as arugment
#print 1 first, then 0.
#the length of string is whatever the integer is

def stringy(num):
    number_string = ''
    for _ in range (num):
        if len(number_string) % 2 == 1:
            number_string += '0'
        elif len(number_string) % 2 == 0:
            number_string += '1'
    return number_string

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
