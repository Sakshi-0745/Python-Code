num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
num3 = int(input("enter a number"))
numbers = [num1,num2,num3]
"""
#method 1 : it will print the sum of non duplicate numbers and it will ignore the duplicate numbers and print the number
unique_numbers = [num for num in numbers if numbers.count(num) == 1]
result = sum(unique_numbers)
print(result)
"""
"""
# it will print the sum of non duplicate value and if duplicate value it will ignore 1 duplicate value and print the sum of other 2 values
if num1 == num2 or num2 == num3 or num1 == num3:
  numbers = sorted([num1,num2,num3])
  result = numbers[0] + numbers[1]
  print(result)
else:
  result = num1 + num2 + num3
  print(result)
  """
# using if_else
if (num1!= num2 and num2 != num3 and num1 != num3):
    print(num1 + num2 + num3)
else:
    if num1 == num2:
        print(num3)
    elif num2 == num3:
        print(num1)
    else:
        print(num2)
