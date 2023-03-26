("""Write a program to create lambda function to add two numbers and display total.""")

m=int(input("Enter any number : "))
n=int(input("Enter any number : "))

x = lambda a, b : a + b
print("Addition is : ",x(m, n)) 