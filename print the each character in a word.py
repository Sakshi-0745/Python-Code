with open(r"C:\Users\LENOVO\OneDrive\Desktop\sakshi\my_file.txt") as file:
    lines = file.readlines()
    for line_number, line in enumerate(lines, start=1):
        character_count = 0
        for char in line:
            print(char)
            character_count += 1
    print(f"Total characters in line {line_number}: {character_count}")