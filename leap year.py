year=int(input("Enter a year"))
if (year%4) == 0 :
    if (year%100) == 0 :
        if (year%400) == 0:
            print("year is leap year")
        else:
            print("year is not a leap year") 
    else:
        print("yea is not a leap year")
else:
    print("year is not a leap year")           