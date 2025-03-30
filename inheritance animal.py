class animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
class dog(animal):
        def speak(self):
            return self.name + " says woof"
class cat(animal):
        def speak(self):
            return self.name + " says meow"
dog = dog("goldy")
cat = cat("kitty")
print(dog.speak())
print(cat.speak())