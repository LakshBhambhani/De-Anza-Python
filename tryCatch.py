word = "Python"
try:
    a = 10/0
    print(a)
except ZeroDivisionError:
    print("Diving by  0")
for i in word:
    print(i)


try:
    import hello
except ImportError:
    print('Import error')