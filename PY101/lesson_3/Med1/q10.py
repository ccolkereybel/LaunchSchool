a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

#id(a) == id(b) because same number - interning

#id(c) would also be the same because points to 42

#True