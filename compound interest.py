def calculate_compound_interest(principal, rate, time):
    rate_decimal = rate / 100
    total_amount = principal * (1 + rate_decimal) ** time
    return total_amount
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate:"))
time = float(input("Enter the time in years:"))
calculate_compound_interest = calculate_compound_interest(principal, rate, time)
print(f"The total amount after {time} years is: {calculate_compound_interest:.2f}")

