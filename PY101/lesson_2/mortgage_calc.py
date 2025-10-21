def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f'Value must be > 0: {number_str}')
    except ValueError:
        return True

    return False

prompt("Let's calculate your car monthly payments!")

while True:
    prompt("------------------------------------------")

    prompt("What is your total loan amount? Enter the dollar amount")

    amount = input()
    while invalid_number(amount):
        prompt('Must be a positive number')
        amount = input()

    prompt("What is your interest rate?")
    prompt("Example: 5 for 5% or 2.5 for 2.5%")

    interest_rate = input()

    while invalid_number(interest_rate):
        prompt("Must be a positive number")
        interest_rate = input()


    prompt("What is the duration of the loan in years?")
    years_duration = input()

    while invalid_number(years_duration):
        prompt("Must be a positive number")
        years_duration = input()

    loan_amount = float(amount)
    annual_interest_rate = float(interest_rate) / 100
    months = float(years_duration) * 12
    monthly_interest__rate = annual_interest_rate / 12

    monthly_payment = loan_amount * (
        monthly_interest__rate /
        (1 - (1 + monthly_interest__rate) ** (-months))
    )

    prompt(f"Your monthly payment is: ${monthly_payment: .2f}")

    prompt("Would you like to do another calculation? (y/n)")

    answer = input()

    if answer and answer[0].lower() != 'y':
        break
