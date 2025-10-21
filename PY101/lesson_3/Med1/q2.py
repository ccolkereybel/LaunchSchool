def factors(number):
    if number < 0:
        return 'please enter a positive number'
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    
    return result

print(factors(-20))


#number % divisor == 0 checks that it goes in evenly with no remainer