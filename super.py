 # super keyword

# super

# base class

class Animal:
    def __init__(self):
        self.name = "Bunny"

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks . it is a {self.breed} breed")

dog = Dog("Golden Retriever")
dog.speak()     

# output
# Bunny makes a sound
# Bunny barks . it is a Golden Retriever breed

    

