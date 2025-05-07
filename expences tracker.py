FILENAME = "expenses.txt"

def add_expense():
    amount = input("Enter amount: ")
    reason = input("Enter reason: ")
    with open(FILENAME, "a") as file:
        file.write(f"{amount},{reason}\n")
    print("Expense added!")

def view_expenses():
    try:
        with open(FILENAME, "r") as file:
            total = 0
            print("\nYour Expenses:")
            for line in file:
                amount, reason = line.strip().split(",")
                total += float(amount)
                print(f"{reason}: ₹{amount}")
            print(f"\nTotal Spent: ₹{total}")
    except FileNotFoundError:
        print("No expenses found.")

def main():
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
