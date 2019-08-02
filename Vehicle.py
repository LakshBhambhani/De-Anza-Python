class Vehicle():
    def __init__(self, fuelAmount, capacity, applyBrakes):
        self.fuelAmount = fuelAmount
        self.capacity = capacity
        self.applyBrakes = applyBrakes

    def fuelAmount(self):
        return self.fuelAmount()

    def capacity(self):
        return self.capacity()

    def applyBrakes(self):
        return self.applyBrakes()


class Bus(Vehicle):
    def getNumberWheels(self):
        return 4

class Car(Vehicle):
    def getNumberWheels(self):
        return 4

class Truck(Vehicle):
    def getNumberWheels(self):
        return 16