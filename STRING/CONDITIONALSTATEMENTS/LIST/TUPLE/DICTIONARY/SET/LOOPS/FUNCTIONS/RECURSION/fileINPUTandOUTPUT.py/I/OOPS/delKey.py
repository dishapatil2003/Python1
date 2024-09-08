#del keyword -- > used to delete object properties or object itself.

class Student:
    def __init__(self,name):
        self.name = name


s1 = Student("disha")

del s1
print(s1)