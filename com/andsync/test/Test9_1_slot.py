class Student(object):
    __slots__ = ('age', 'name')
    pass
s=Student()
s.name="Michael"
print(s.name)


def set_age(self, age):
    self.age = age
from types import MethodType
s.set_age= MethodType(set_age, s)
s.set_age(33)
print(s.age)

s2=Student()
s2.set_age(23)
print(s2.age)

def set_score(self,score):
    self.score=score
Student.set_score=set_score
s.set_score(100)
print(s.score)
