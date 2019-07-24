class Dog:
    def  __init__(self,  breed, size, age, color):
        self.breed = breed
        self.size = size
        self.age  = age
        self.color  = color
        print("I'm a", age, "year old", size,  color, breed)

    def eat(self):
        print("I'm Eating")

    def sleep(self):
        print('I\'m sleeping')

    def sit(self):
        print("I'm sitting")

    def run(self):
        print("I'm running")


dog1 = Dog("Neapolitan mastiff", "Large", 5, "Black")
dog2 = Dog("Maitise", "Small", 2, "WHite")
dog2 = Dog("Chow Chow", "Medium", 3, "Brown")