# simple inheritance

# base class

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# drived class
class Dog(Animal):
    def __init__(self,pet):
        self.behaviour = "friendly"
        self.bunny = pet

    def speak(self):
        print(f" {self.bunny} barks. He is very {self.behaviour}")


# creat an instance/object of Animal class
# animal = Animal("General animal")
# animal.speak()                # output : General animal makes a sound

# creat an instance/object of Dog class
dog = Dog("dadu")
dog.speak()                   # output : Buddy barks



# Dog.__init__() missing 1 required positional argument: 'pet'


# override the function when function have same method name.
# we are inheriting  the Base class(Animal Class) methods and attributes in  the drived class(Dog class)
# now the object/instance of drived class will be able to access the attribute of parent class (base class)
# and also the methods of parent class