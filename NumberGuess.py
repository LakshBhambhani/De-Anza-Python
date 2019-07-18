from random import randint
running = True

while running:
    guess = int(input("Enter a number to see if it's right"))
    rand = randint(1, 10)
    if guess == rand:
        print("You have guessed it correctly")
    elif guess < rand:
        print("The number guessed was smaller than the number chosen")
    elif guess  > rand:
        print("The number guessed was bigger than the  number chosen")

    response = str(input("Try Again?"))
    if response == "yes":
        running = True
    else:
        running = False

print("Exited Game! Thank you!")