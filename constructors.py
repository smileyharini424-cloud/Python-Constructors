class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print()


student1 = Student("Harini", 20, "CSE")
student2 = Student("Anu", 21, "ECE")

student1.display()
student2.display()
