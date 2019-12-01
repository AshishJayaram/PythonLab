class Person:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;


p1 = Person("Supandi", 14)

print("\nName of person is ", p1.name)
print("\nAge of person is ", p1.age)

print("\n****Printing after deleting age attribute for p1****")
del p1.age
print("\nName of person is ", p1.name)

print("\n****Printing after deleting p1****")
del p1
#print("\nName of person is ", p1.name)
