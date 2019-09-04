class Student:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    marks=["91","92","93"];

p1=Student("Sponge",20,)
#p2=Student("DFJ",20)

def Display(Student):
    print("\nName of person is ", p1.name)
    print("\nAge of person is ", p1.age)
    print(Student.marks)

Display(Student)
