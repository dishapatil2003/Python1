#private attributes & methods are meant to be used only within the class and are not accessible from outside the class
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # private attribute

acc1 = Account("12345","abcde")
print(acc1.acc_no)  # prints: 12345