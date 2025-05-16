password = input("Enter password: ")

if len(password) < 6:
    print("Too short")
elif password.isnumeric() or password.isalpha():
    print("Weak password")
else:
    print("Strong password")
