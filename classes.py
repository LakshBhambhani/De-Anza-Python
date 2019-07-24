class FirstClass:
    name = "python"

    def helloFunction(self):
        print("hello from my method")

#creating an object or instantiation

object1 = FirstClass()
print(object1.name)
object1.helloFunction()


class Shark:
    def swim(self):
        print(self.name, " in swim method")
        print('sharks can swim')

    def beAwesome(self):
        print("im in beAwesome method")
        print('sharks are awesome')

    def __init__(self, name):
        self.name   = name
        print("This is the constructor method")


shark1 = Shark("samu")
shark2 = Shark("helo")
