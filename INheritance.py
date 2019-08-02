class Person():
    def __init__(self, name):
        self.name = name

    def isEmployee(self):
        return False

    def isStudent(self):
        return False

class Student(Person):
    def isStudent(self):
        return True

class Employee(Person):
    def isEmployee(self):
        return True

student1 = Person("abc")
student2 =  Student("Max")

print(student1.isStudent())
print(student2.isStudent())