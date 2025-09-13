num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def gcd(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd = i
    return gcd
print("The GCD of", num1, "and", num2, "is", gcd(num1, num2))