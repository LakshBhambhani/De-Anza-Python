#  defining  a simple  function

def hello():
    print("Hello World")

def square(n):
    return n*n

myList = [1, 23, 4, 6, 78]
result = map(square, myList)

print(list(result))

result = map(lambda x:x*x, myList)
print(list(result))

list1 = [1, 2, 3, 5]
list2 = [3,  5, 6,  7]

result = map(lambda x, y: x+y, list1, list2)
print(list(result))