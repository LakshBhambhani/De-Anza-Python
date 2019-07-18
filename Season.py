# User enters month number and day number to check what season it is

month = int(input("Enter the month number"))
day = int(input("Enter the day number"))

if(month >= 12 and month <= 2 and day >=1 and day <= 31):
    print("It's Winter")
elif(month >= 3 and month <= 5 and  day >=1 and day <=31):
    print("It's spring")
elif(month >= 6 and month <= 8 and  day >= 1 and day <= 31):
    print("it's summer")
else:
    print("It's Fall")