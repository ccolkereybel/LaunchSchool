#function takes string argument
#return new string with all consecutive duplicate chars removed
#for each letter, if the letter next to it is the same, strip that letter

def crunch(string):
    letter_list = ''

    if len(string) == 1 or string == '':
        return string

    for letter in range(0, len(string)-1):
        if string[letter] != string[letter + 1]:
            letter_list += string[letter]
   
    letter_list += (string[-1])
    
    return letter_list

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')