class Student(object):
    name="Student"
    def __init__(self,name):
        self.name=name;
s=Student("Bob")
s.age=30
print(s.name)
print(Student.name)

class Teacher(object):
    count=0
    def __init__(self,name):
        self.name=name
        Teacher.count+=1
t=Teacher("zhangsan")
t1=Teacher("zhangsan")
t2=Teacher("zhangsan")
t3=Teacher("zhangsan")
print(Teacher.count)
