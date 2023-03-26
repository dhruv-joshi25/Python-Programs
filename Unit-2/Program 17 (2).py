("""Write a program to create dictionary in such a way that it should add number
as a key and square root of number as a value between 1 to n in the dictionary...
At the end, the data shall be displayed.
Example : {1:1, 2:4, 3:9, 4:16, 5:25, ...}""")

var=int(input("Enter any number : "))

d=dict()
for x in range(1,var+1):
    d[x]=x**2
print(d)  


