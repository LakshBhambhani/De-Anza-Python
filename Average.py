# Calculate average of 10 numbers entered by the user

x = 1
numbers = []

for x in range(10):
    number = int(input("Enter a number"))
    numbers.append(number)

sum = 0
for x in range(10):
    sum = sum + numbers[x]
answer = sum / 10
print("The average is")
print(answer)