def evenOdd(a):
    if a % 2 == 0:
        return "It's Even"
    else:
        return "it's Odd"

def primeNumber(a):
    x = 1
    factors = []
    while x <= a:
        if a % x ==0:
            factors.append(x)
        x += 1
    if len(factors) ==2:
        return "It's Prime"
    else:
        return "It's Composite"

def positiveNumber(a):
    if a > 0:
        return "It's Positive"
    elif a < 0:
        return "It's Negative"
    else:
        return "It's 0"

num1 = int(input("Enter a number to check if its even or odd"))
print(evenOdd(num1))

num2 = int(input("Enter a number to check if it's prime or composite"))
print(primeNumber(num2))

num3 = int(input("Enter a number to check if it's positive, negatie or 0"))
print(positiveNumber(num3))

def hello():
    print("Hello")

def helloName(a):
    if len(a) > 0:
        print("Hello", a)
    else:
        print("Hello World")

helloName()
