class Animal:
    def make_sound(self):
        print("Some generic animal")


class Dog(Animal):
    def make_sound(self):
        print("Bow Bow")
        
class Cat(Animal):
    def make_sound(self):
        print("Mow Mow")
        

animals = [Dog(), Cat()]

for an in animals:
    an.make_sound()