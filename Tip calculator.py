import random
amount = int (input("Enter the amount of bill: "))
tip = int(input("Enter the tip percentage:"))
tip = amount + (amount / 100)* tip
peoples = int (input("Enter no of peoples :"))
print("Each person has to pay : ",tip/peoples)
print("Total amount to be payed : ", tip)