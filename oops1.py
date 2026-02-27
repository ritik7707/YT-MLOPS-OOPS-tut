#initiate a class

class Employee:
    def __init__(self):           # magic method , dunder method - constructor
        print("started executing attributes/data")
        self.id = 123
        self.salary = 40000
        self.designation = "SDE"
        print("attributes/data has been initiated")

    def  travel(self ,destination):
        print("This travel method called manually")
        print(f"Employee in now travelling to {destination}")


# create an object/instance of the class

sam = Employee()
# printing the attributes

# print(sam.id)
# print(sam.salary)
# print(sam.designation)

# calling a method 
# sam.travel("Delhi")

print(type(sam))

                        