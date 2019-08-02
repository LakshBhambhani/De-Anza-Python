import random

# class Dog:
#     def walk(self):
#         print("walking")
#
# class JackRussellTerrier(Dog):
#     def speak(self):
#         return "Arff!"
#
# bobo = JackRussellTerrier()
# bobo.walk()
#
# a = input("Enter a string")
# b = input("Enter a substring to check if it's present in the first string")
#
# if a.__contains__(b):
#     print("Substring is present")
# else:
#     print("Substring is not present")

# multiply_by_two = lambda x: x * 2
# numbers = [1, 2, 3]
# doubled = map(multiply_by_two, numbers)
# doubled_list = list(doubled)
# print(doubled_list)

# nums = [3, 5, 16, 27]
# some_nums = list(filter(lambda num: num < 10, nums))
# print(some_nums)

# letters = ["beach", "car"]
# funified = list(map(lambda word: f"{word} is fun!", letters))
# print(funified)

# add_one = lambda x: x + 1
# print(add_one(7))
#
# print(random.seed(3))
# a = random.seed(3)
# print(a)

#fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
#
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
#
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
#
# print (sum)
#
# def printLine(text):
#  	print(text, 'is awesome.')
# printLine('Python')

# def add():
#     x = 1
#
# a = add()
# print(a)

# def greetPerson(name):
#     print('Hello', name)
# greetPerson('Frodo', 'Sauron')

# def Foo(x):
#  	if (x==1):
#    		return 1
#  	else:
#    		return x+Foo(x-1)
# print(Foo(4))

numbers = [1, 3, 6]
newNumbers = tuple(map(lambda x: x , numbers))
print(newNumbers)





