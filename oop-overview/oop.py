#definition of the class
class Student:

    #invoking the constructor of the class
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #functions inside classes are called methods
    def get_student_details(self):
        return f'{self.name} aged {self.age}'
    
class Academics:

    def __init__(self,status,grades,year,student:Student):
        self.status=status
        self.grades=grades
        self.year=year
        self.student=student

    def get_academic_info(self):
        return f'{self.student.get_student_details()} has {self.status} his exams for session {self.year} and was graded {self.grades}'

#creating object for the class student
std=Student('Ram Karki',24)
#creating object for the class Academics and add student object
acdm=Academics('passed','B+',2023,std)

#using object to access the method of the class
print(acdm.get_academic_info())