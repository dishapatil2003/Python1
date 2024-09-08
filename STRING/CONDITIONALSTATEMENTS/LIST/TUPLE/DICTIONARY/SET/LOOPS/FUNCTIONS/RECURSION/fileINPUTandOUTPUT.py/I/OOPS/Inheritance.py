#When one class(child/derived) derives the properties & methods of another class(parent/base)

class Car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuer")
car2 = ToyotaCar("prius")

print(car1.start())