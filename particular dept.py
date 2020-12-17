class student:
    def __init__(self,name,rollno,course,year):
        self.name = name
        self.rollno = rollno
        self.course = Course(course,year)
    def show(self):
        print(self.name,self.rollno)
        print(self.course.get())
class Course:
    def __init__(self,name,year):
        self.name = name
        self.year = year
    def get(self):
        return(self.name,self.year)
class Deptt:
    def __init__(self,name):
        self.name = name
        self.courses = []
        def get(self):
            return(name, courses)
        def add_courses(self,name):
            self.courses.append(name)
        def show_courses(self):
            print("courses offered in this department are:",self.courses)
D1=Deptt("mathematics")
D2=Deptt("computer science")
D1.add_courses("BA(H)")
D1.add_courses("BSE(H)")
D2.add_courses("BCA")
D2.add_courses("BTech")
print("***Dear students the list of courses offreed in their respective departments is given beow..Kindly choose any one course***")
D1.show_courses()
D2.show_courses()
S=Student("Harman",1234,"BCA",2017)
S.show()

        
