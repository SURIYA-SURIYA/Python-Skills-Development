print("Year Is Leap year or not");

year = int(input("Enter The year : "));

if (year % 4 ==0 & year % 400 ==0 & year % 100 !=0):
    print(year,"is a leap year");
else:
    print(year,"is not a leap year");