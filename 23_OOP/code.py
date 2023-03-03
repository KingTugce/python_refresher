class Student():

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Jimmy", (100,100,98,87,99))
student2 = Student("Rolf", (90,80,78,98,98))

print(student.average_grade())
print(student2.average_grade())

