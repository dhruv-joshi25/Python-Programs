#Write a program to input a number and display Factorial of that number.
#For example,Factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120.

fact=int(input("Enter Any Number You want to factrial of : "))
    
for i in range(1,fact):
    fact=fact*i
    print(fact)
