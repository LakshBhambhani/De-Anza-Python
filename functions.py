def sayHello(name):
    print("Hello", name)
    return

name = input("Enter your name")
sayHello(name)

#Performing sum of numbers

def addNum(a, b):
    c = a +b
    return c, a, b

print(addNum(2, 3))

# pass list as a parameter

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [2, 3, 4]

def addNumFromList(list1):
    for x in list1:
        print(x)

addNumFromList(list2)

# Definining lambda or anonymous function

square = lambda x: x*x
print(square(5))

def squares(x):
    return x*x

print(squares(5))

a = input("ENter a string")
print(len(a))

print()

# Printing string in all uppercase letters

print(a.upper())
print(a.split(" "))

b = input("ENter a group of words")

words = b.split(" ")
print(words)
c=''
for x in range(len(words)):
    c += words[x]
    if x < len(words) - 1:
        c += '-'


print(c)

name = input("Enter your name")
names = name.split(' ')
final = ''
for x in range(len(names)):
    final += names[x].capitalize()
    final += " "

print(final)
