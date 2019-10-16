
class Student:
    def __init__(self,name,age,marks):
        self.name=name;
        self.age=age;
        self.marks=marks;

p1=Student("Sponge",20,[91,92,93])
#p2=Student("DFJ",20)

def Display(Student):
    print("\nName of person is ", p1.name)
    print("\nAge of person is ", p1.age)
    print("\nMarks are ",p1.marks)

Display(Student)
