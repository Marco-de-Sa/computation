class Person:
    # the constructor method of the Person class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # to string function of the person class
    def __str__(self):
        return f"{self.name}({self.age})"

# creates an object of the Person class named p1
p1 = Person("John", 36)

# printing the p1 object like this automatically calls the __str__function of the Person class
print(p1)