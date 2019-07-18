# Python program to find hcf and lcm of entered numbers

num1 = int(input("Enter number 1 to find it's HCF and LCM"))
num2 = int(input("Enter number 2 to find it's HCF and LCM"))

if num1 > num2:
    smaller = num1
    greater = num2
else:
    smaller = num2
    greater = num1

x = 1
hcf = 0
while x <= num1:
    if  num1 % x == 0 and num2 % x == 0:
        hcf = x
    x += 1

print("HCF of ", num1, " and ", num2, " is ", hcf)

lcm = int((num1 * num2) / hcf)

print("LCM of ", num1, " and ", num2, " is ", lcm)