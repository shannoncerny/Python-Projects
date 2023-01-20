
# creates parent class
class Student:
    def __init__(self, name, age, grade):
        self.age = age
        self.grade = grade

#creates child class, inherits attributes from parent class
class Student1(Student):
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

#creates child class, inherits attributes from parent class
class Student2(Student):
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

#adds attributes to Student class
student1 = Student('Ann',15,10)
student2 = Student('Ben',17,12)
