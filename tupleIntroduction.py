# INtroduction to tuples

import sys
import timeit

mytuple = ("apple", "cherry", "orange")
print(mytuple)
languages = ("java", "python", "perl", "c")
combinedtuples = languages + mytuple
print(combinedtuples)

combine = (mytuple, languages)
print('nesting tuples', combine)

# iterate through tuple using for loop

for i in languages:
    print(i)

print(languages[1:4:2])

#reverse tuple using negative indexing

print(languages[::-1])
single_element = (1, )
print(type(single_element))
print(len(single_element))

primenums = [2, 3, 5, 7, 11]
squares = (1, 4, 9, 16, 25)

# testing length function on tuple and list

print(len(primenums))
print(len(squares))

# iterating in both tuple in list

for p in primenums:
    print(p)

for s in squares:
    print(s)

# testing methods for tuples and lists

print("Testing methods for list")

print(dir(primenums))
print(dir(squares))

# tesing which one uses less space on disk

listSize = sys.getsizeof(primenums)
tupleSize = sys.getsizeof(squares)

print(listSize)
print(tupleSize)

# Hence list takes up more space on disk and tuples are bettter to save some space

# time tests on tuples and lists

listTest = timeit.timeit(stmt="[2, 3, 5, 7, 11]", number=1000000)
tupleTest = timeit.timeit(stmt="(1, 2, 4, 9, 16)", number=1000000)
print(listTest)
print(tupleTest)

a = 5.1
b = 0 + 3j
c = a + b
print(c)

n=6
if 5 < n <= 10:
    print("True")

word = 'Problem'
print(word[::-1])

a = 'coffee'
b = 'it\'s'
c = 'hot!'
d = ','

word1 = 'she said "' + a + d + ' ' + b + ' ' + c + '"'
print(word1)


e = 'C:\\Users\\Gabby\\Documents'
print(e)

problem = []
for x in range(len(word)):
    problem.append(word[x])

print(problem)

word2 = 'rotten tomatoes'

print(word2[3:6:])

number = [6]
print(bool(number))

letter = ['C', 'D', 'R']
print(letter[0], letter[1])

numbers = []
for x in range(10):
    numbers.append(x + 1)

print(numbers)
print(numbers[1::2])
print(numbers[0::2])
print(numbers[::-1])

list1 = ['one', 'two', 'three']
tuple1 = ('one', 'two', 'three')

list1[1] = '2'
print(list1)
lst = list(tuple1)
lst[1] = '2'
tuple1 = tuple(lst)
print(tuple1)

x = 0.0
print(bool(x))