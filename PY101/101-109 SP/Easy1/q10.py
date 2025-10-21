def multisum(number):
    multiple_3 = list(range(3, number + 1, 3))
    multiple_5 = list(range(5,number + 1, 5))
    all_multiples = set(multiple_3 + multiple_5)
    return (sum(all_multiples))
   


# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)