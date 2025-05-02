import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return "Invalid currency code."
    
    rate = data["rates"].get(to_currency.upper())
    if rate:
        converted = amount * rate
        return f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}"
    else:
        return "Target currency not found."

# Example usage
amount = float(input("Enter amount: "))
from_currency = input("From currency (e.g., USD): ")
to_currency = input("To currency (e.g., INR): ")

result = convert_currency(amount, from_currency, to_currency)
print(result)
