#function takes num as argument
#if num positive, return neg of that number
#if num neg, return as is


def negative(num):
    return -abs(num)
    
print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True