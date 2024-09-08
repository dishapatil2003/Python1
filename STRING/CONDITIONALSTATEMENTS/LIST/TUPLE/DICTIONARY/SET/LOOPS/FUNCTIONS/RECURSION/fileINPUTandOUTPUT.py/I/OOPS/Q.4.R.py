#Define a Employee class with atrributes role,department and salary  . This class also have showDetail() methpd.
#craete a engineer class that inherits properties from Employee and


class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)

        class Engineer(Employee):
            def __init__(self,name,age):

                self.name = name
                self.age = age
                super().__init__("Engineer","IT","75000")

e1 = Employee("accountant","Finance","60000")
e1.showDetails()