(""""Write a Python Program that creates a Student class with various methods.
Use setattr() and getattr() on class object.""")

class student:
    name = "Dhruv"
    roll_no = 101
    address = "Gondal"

std = student()

setattr(std, "name" , "Dhruv")
a = getattr(std, "name")
print(a)

setattr(std , "roll_no", 101)
b = getattr(std, "roll_no")
print(b)

setattr(std , "address", "Gondal")
b = getattr(std, "address")
print(b)