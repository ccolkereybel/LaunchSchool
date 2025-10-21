bill_amount = float(input('What is the bill amount? '))
tip_percentage = float(input('What percent tip would you like to leave? '))

tip_as_decimal = tip_percentage/100
tip_amount = bill_amount * tip_as_decimal
bill_with_tip = bill_amount + tip_amount

print(f'The tip is {tip_amount:.2f}') 
print(f'The total is {bill_with_tip:.2f}')