string1 = input("Enter first string: ")
string2 = input("Enter second string: ")    
if (len(string1) != len(string2)):
    print("The strings are not anagrams.")
else:
    string1 = sorted(string1)
    string2 = sorted(string2)
if  (string1 == string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")