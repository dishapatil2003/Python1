# __init__Function
#Constructor
#All classes have a function called_init_(),which is always exeuted when the object is being initiated.

class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database...")


s1 = Student("disha",97)
print(s1.name)

s2 = Student("sanket",98)
print(s2.name,s2.marks)