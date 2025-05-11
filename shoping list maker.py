shopping_list = []

while True:
    item = input("Add item (or type 'done'): ")
    if item.lower() == "done":
        break
    shopping_list.append(item)

print("\nYour Shopping List:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")
