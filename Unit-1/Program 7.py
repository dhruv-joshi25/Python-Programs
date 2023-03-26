#Write a program to input age of person and display message as follows
#-If age < 12 print You are Kid
#-If age between 12 to 17 print You are teenager
#-If age between 18 to 60 print you are Adult
#If age > 60 print You are Senior Citizen


age=int(input("Enter Age : "))

if age<=12:
    print("You are kid.")
elif age > 12 and age<=17:
    print("you are a teenager.")
elif age>18 and age<60:
    print("you are an adult")
else:
    print("you are senior citizen") 
