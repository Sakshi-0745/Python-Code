num1 = int(input("enter a nummber"))
num2 = int(input("enter a nummber"))
num3 = int(input("enter a nummber"))
if num1>num2 and num1>num3:
    print("largest number is",num1)
elif num1<num2 and num2>num3:
    print("largest number is",num2)
else:
    print("largest number is",num3)