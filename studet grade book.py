def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'
gradebook = []

while True:
    name = input("Enter student name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    try:
        marks = float(input(f"Enter marks for {name}: "))
        grade = calculate_grade(marks)
        gradebook.append({"Name": name, "Marks": marks, "Grade": grade})
        print(f"{name} got a grade of {grade}")
    except ValueError:
        print("Please enter valid marks")