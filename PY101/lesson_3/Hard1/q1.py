def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

#no first will return prop1: 'hi there', the second has nothing to return and then a dictionary
#just printed that wont be accessed
