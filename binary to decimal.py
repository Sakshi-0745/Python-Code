def binary_to_decimal(binary):
  decimal = 0
  power = 0
  for digit in binary[::-1]:
    decimal += int(digit) * 2 ** power
    power += 1
  return decimal
binary = input("Enter a binary number to convert: ")
decimal = binary_to_decimal(binary)
print("The decimal equivalent of {0} is {1}".format(binary,decimal))