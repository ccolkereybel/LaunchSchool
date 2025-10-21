#return second to last word in a string

def penultimate(string):
    words_list = string.split()
    return words_list[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")