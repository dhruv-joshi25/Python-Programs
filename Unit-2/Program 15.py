("""Write a program to print factorial number using function""")

def factorial(num):
    """
    Calculate the factorial of a number.
    """
    # handle edge cases where num is 0 or 1
    if num == 0 or num == 1:
        return 1
    # calculate the factorial using a loop
    else:
        result = 1
        for i in range(1, num+1):
            result *= i
        return result

# get the input from the user
n = int(input("Enter a number: "))

# calculate the factorial using the factorial function
result = factorial(n)

# print the result
print(f"The factorial of {n} is {result}")
