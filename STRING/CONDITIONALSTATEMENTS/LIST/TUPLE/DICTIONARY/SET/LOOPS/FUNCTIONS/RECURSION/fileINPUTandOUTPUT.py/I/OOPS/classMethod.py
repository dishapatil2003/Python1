#A class method is bound to the class & receives the class as an implicit first argument.

class Person:
    name = "anonymous"

    def changeName(self,name):
        Person.name = name
p1 = Person()
p1.changeName("disha")
print(p1.name)



