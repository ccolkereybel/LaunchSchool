#get user age from input
#get retirement age
#print current year and the year they will retire
#print how many years left to work

import datetime

age = int(input('What is your age? '))
retirement_age = int(input('At what age would you like to retire? '))

current_year = datetime.datetime.now().year
years_until_retirement = retirement_age - age

print(f"It's {current_year}. You will retire in {current_year + years_until_retirement}")
print(f"You only have {years_until_retirement} years of work to go!")