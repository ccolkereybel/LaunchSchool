pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys() #Cat, Dog, Bird
del pets['Dog'] #Cat: Meow, Bird: Tweet
pets['Snake'] = 'Sssss'
print(keys) #dict_keys()