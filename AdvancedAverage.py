# Calculate average of 10 numbers entered by the user

x = 1
numbers = []

running = True

while running:
    cont = str(input("Want to quit after this? Enter q"))
    if (cont == "q"):
        running = False;
        break
    number = int(input("Enter a number"))
    numbers.append(number)

try:
    sum = 0
    product = 1
    for x in range(len(numbers)):
        sum = sum + numbers[x]
    for x in range(len(numbers)):
        product = product * numbers[x]
    answer = sum / len(numbers)
    print("The average is")
    print(answer)
    print("The product is")
    print(product)
except ZeroDivisionError:
    print("Zero Division Error occured")
