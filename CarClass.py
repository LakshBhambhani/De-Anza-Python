class  Car:
    def  __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model
        print("A new", color, make, model, 'was instantiated')

    def applyBraking(self):
        self.braking = True

    def openMoonroof(self):
        self.openMoonroof = False

    def speed(self, speed):
        self.speed = speed


file = open("car.txt", "r")
text =  file.read().split('\n')

colorString  = text[0]
makeString = text[1]
modelString = text[2]

color = colorString.split(',')
make  = makeString.split(',')
model = modelString.split(',')

cars  = list()
for x in range(0, len(color)):
    cars.append(Car(color[x], make[x],  model[x]))

choice = int(input("Enter a choice 1 or 2 or 3"))
print('========================================')
print('Here is your choice')
if choice == 1:
    number = 0
elif choice == 2:
    number = 1
else:
    number = 2

print('Color:', color[number])
print('Make:', make[number])
print('Model:', model[number])