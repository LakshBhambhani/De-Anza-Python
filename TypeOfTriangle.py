# Program to check the type of a triangle a.k.a equilateral, isoceles or scalene

side1 = int(input("Enter length of side 1"))
side2 = int(input("Enter length of side 2"))
side3 = int(input("Enter length of side 3"))

if(side1 == side2 == side3):
    print("It's an Equilateral Triangle")
elif(side1 == side2 or side1 == side3 or side2 == side3):
    print("It's an isoceles triangle")
else:
    print(("It's a scalene triangle"))