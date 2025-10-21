#write function that takes string as argument
#remove nonalpha characters
#replace with space

def clean_up(string):
    clean_string = ''

    for index, letter in enumerate(string):
        if letter.isalpha():
            clean_string += letter  
        elif not clean_string.endswith(" "):
            clean_string += ' '
            
    return clean_string

print(clean_up("---what's my +*& line?") == " what s my line ")
