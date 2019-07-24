import random

computerValue = ""
def computerTurn():
    rand = random.randint(1, 3)
    if rand == 1:
        computervalue = "Rock"
    elif rand == 2:
        computerValue = "Paper"
    elif rand == 3:
        computerValue = "Scissors"

def rock(a):
    if a == "Rock":
        return "Both are Rock"
    elif a == "Paper":
        return "Computer is a paper and it grabbed you"
    else:
        return "You win! Computer was a scissor"

def paper(a):
    if a == "Rock":
        return "You win! Computer was a rock"
    elif a == "Paper":
        return "Both are paper"
    else:
        return "Computer wins! Computer was a scissor"

def scissor(a):
    if a == "Rock":
        return "You win! Computer was a rock"
    elif a == "Paper":
        return "You win! Computer was a paper"
    else:
        return "Both are scissors"


userInput = ""
while userInput != "quit":
    userInput = input("Enter Rock Paper Scissors or Quit")
    if userInput == "rock":
        result = rock(computerValue)
    elif userInput == "paper":
        result = paper(computerValue)
    elif userInput == "quit":
        print("bye")
        break
    else:
        result = scissor(computerValue)
    print(result)
    computerTurn()

