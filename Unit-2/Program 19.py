("""Write a Python Program to create a function which accepts 3 arguments. (2 numbers and one arithmetic operator). Display answer accordingly.""")

def arithmatic():
    var1=int(input("Enter any number  : "))
    var2=int(input("Enter any number :"))

    op=input("Enter any operation's sign : ")

    if op == '+':
        print("Addition is : ",var1+var2)
    elif op == '-':
        print("Substraction is : ",var1-var2)
    elif op == '*':
        print("Multiplication is : ",var1*var2)
    elif op == '/':
        print("Division is : ",var1/var2)

arithmatic()