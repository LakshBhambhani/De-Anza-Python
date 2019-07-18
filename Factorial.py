# Find a factorial of an entered number

number = int(input("Enter a number to find it's factorial"))\

answer = number

while number > 1:
    answer *= number - 1
    number -= 1

print(answer)