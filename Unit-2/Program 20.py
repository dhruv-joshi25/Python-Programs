("""Write a Python Program to create function which accepts one argument as 
a number and return Factorial value of the number. 
(Function must be RECURSIVE function, not loop)""")

def factorial(num):
    """
    Calculate the factorial of a number using a recursive function.
    """
    # base case: factorial of 0 or 1 is 1
    if num == 0 or num == 1:
        return 1
    # recursive case: multiply num by the factorial of num-1
    else:
        return num * factorial(num-1)

# get the input from the user
n = int(input("Enter a number: "))

# calculate the factorial using the recursive function
result = factorial(n)

# print the result
print(f"The factorial of {n} is {result}")
