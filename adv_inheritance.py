# # single or Basic Inheritance

# # Base class
# class Parent:
#     def __init__(self,name):
#         self.name = name 
    
#     def greet(self):
#         print(f"Hello, my name is {self.name}")

# # Drived class
# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")


# # object/instance of the Child class
# child = Child("Ritik")
# child.greet()
# child.play()

# # output :
# # Hello, my name is Ritik
# # Ritik is playing

# ---------------------------------------------------------------------------------------------- 
# 2. Multilevel inheritance

# # base class 
# class Grandfather:
#     def __init__(self,name):
#         self.name = name

#     def tell_story(self):
#         print(f"{self.name} tell a story")

# # intermediate class
# class Father(Grandfather):
#     def work(self):
#         print(f"{self.name} is working")

# # Derived class
# class Child(Father):
#     def play(self):
#         print(f"{self.name} is playing")



# # create an instance of Child class
# child = Child("Ritik")
# child.tell_story()
# child.work()
# child.play()
# print(child.name)

# # output 
# # Ritik tell a story
# # Ritik is working
# # Ritik is playing
# # Ritik

# ----------------------------------------------------------------------------------------------

# # Hierarchical Inheritance

# # Base class

# class Parent:

#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         print(f"Hello , my name is {self.name}")

# # Drived class 1
# class Child1(Parent):

#     def play(self):
#         print(f"{self.name} is playing")

# # Drived class 2
# class Child2(Parent):

#     def study(self):
#         print(f"{self.name} is studying")

# # Create instances of Child1 and Child2
# child1 = Child1("osama")
# child2 = Child2("sonu")

# child1.greet()       # output: Hello , my name is osama
# child1.play()        # output: osama is playing
# print("\n")          # new line
# child2.greet()       # output: Hello , my name is sonu
# child2.study()       # output: osama is studying


# ----------------------------------------------------------------------------------------------

# Multiple Inheritance (Dimond Problem)

# Common Base class

class A:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello from A, {self.name}")

# Intermediate class 1
class B(A):
    def greet(self):
        print(f"Hello from B, {self.name}")
        super().greet()

# Intermediate class 2
class C(A):
    def greet(self):
        print(f"Hello from C, {self.name}")
        super().greet()

# Drived class

class D(B,C):
    def greet(self):
        print(f"Hello from D, {self.name}")
        super().greet()


# instance of class D
d = D("Frank")
d.greet()
print(D.mro())
# output
# Hello from D, Frank
# Hello from B, Frank
# Hello from C, Frank
# Hello from A, Frank


# Why super() is Important Here

# Without super(), the diamond problem could call A.greet() multiple times.

# Python’s super() + MRO algorithm (C3 Linearization) ensures:

# ✔ each class is called only once
# ✔ correct order is maintained

# Q: What problem does Python solve in multiple inheritance?

# Answer:

# Python solves the Diamond Problem using Method Resolution Order (MRO) and the C3 Linearization algorithm, ensuring each parent class method is called only once

# ----------------------------------------------------------------------------------------------

 
# Hybrid Inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# Intermediate class 1 (Hierarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

# Intermediate class 2 (Multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# Derived class (Multiple Inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)  # Explicitly calling the constructor

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

# Create an instance of Bat
bat = Bat("Bruce")
bat.sound()     # Output: Bruce makes a sound.
bat.feed()      # Output: Bruce is feeding milk.
bat.fly()       # Output: Bruce is flying.
bat.nocturnal() # Output: Bruce is nocturnal.


# Q: What is Hybrid Inheritance?

# Answer:

# Hybrid inheritance is a combination of multiple types of inheritance such as hierarchical and multiple inheritance within the same program.