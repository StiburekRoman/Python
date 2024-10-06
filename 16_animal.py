class Animal:
    def __init__(self, name):
        self._name = name  # privátní proměnná

class Dog(Animal):
    def sound(self):
        print(f"{self._name}: Wof")

class Cat(Animal):
    def sound(self):
        print(f"{self._name}: mňau")

my_dog = Dog('Stark')
my_dog.sound() 

my_cat = Cat('Dizzy')
my_cat.sound()  

print(my_dog._name)  
print(my_cat._name)  