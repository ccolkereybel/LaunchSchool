#return true if 1 and only 1 argument is a truthy
#if only one of the arguments is false, return true

def xor (arg1, arg2):
    if (arg1 and not arg2) or (arg2 and not arg1):
        return True
    else:
        return False
    
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)