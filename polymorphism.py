class Animal:
    def speak(self):
        pass  

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

def make_sound(animal):
    print(animal.speak())


dog = Dog()
cat = Cat()

make_sound(dog)  
make_sound(cat) 
