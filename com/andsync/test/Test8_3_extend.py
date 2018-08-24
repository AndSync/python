
class Animal(object):
    def run(self):
        print("animal run")
    def sing(self):
        print("animal sing")
class Dog(Animal):
    def run(self):
        print("dog run")
    pass
class Cat(Animal):
    def run(self):
        print("cat run")
    pass

class Timer(object):
    def run(self):
        print("ddd")

    def sing(self):
        print("wo sing")
def run_twice(animal):
    animal.sing()
    animal.run()
dog = Dog()
cat = Cat()
timer=Timer()
print(run_twice(dog))
print(run_twice(timer))
