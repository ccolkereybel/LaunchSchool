#function takes string argument
#find the middle character
#find if len even or odd by dividing by 2 and seeing if there is a remainders
#if odd number of characters, return 1 character --> this is the index int of len/2
#if even number of characters, return 2 characters --> this is the index len/2 and len/2-1


def center_of(string):
    middle_index = len(string) // 2

    if len(string) % 2:
        return string[middle_index]
    else:
        return string[middle_index - 1 : middle_index + 1]
    
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True