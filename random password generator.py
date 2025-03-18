import random
import string
length = int(input("enter the length of password"))
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters))
for i in range(length-1):
    password += random.choice(characters)
print(password)