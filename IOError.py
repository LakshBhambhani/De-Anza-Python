try:
    f = open("testing.txt", "r")
    print(f.read())

except IOError:
    print("IO Error! File not found")