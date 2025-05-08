temp = float(input("Enter temperature: "))
unit = input("Is this in (C)elsius or (F)ahrenheit? ").upper()

if unit == "C":
    print(f"{temp}°C = {(temp * 9/5) + 32}°F")
elif unit == "F":
    print(f"{temp}°F = {(temp - 32) * 5/9}°C")
else:
    print("Unknown unit.")
