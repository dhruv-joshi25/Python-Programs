#Write a Python Program to input marks of 4 subjects and display Total, Percentage, Result and Grade.
#If student is fail (<40) in any subject then Result should be displayed as “FAIL” and Grade should be displayed as “With Held**”

def result():
    sub1=int(input("Enter marks Of Subject 1 : "))
    sub2=int(input("Enter marks Of Subject 2 : "))
    sub3=int(input("Enter marks Of Subject 3 : "))
    sub4=int(input("Enter marks Of Subject 4 : "))

    sum=sub1+sub2+sub3+sub4
    print("Total of All marks is    : ",sum)

    per=sum/4
    float(per)
    print("Percentage Is : ",per)

    if sub1<40 or sub2<40 or sub3<40 or sub4<40:
        print("you are fail")
    else:
        if per>=80:
            print("Grade A")
        elif per<=79 and per>=60:
            print("Grade B")
        elif per<=59 and per>=50:
            print("Grade C")
        else:
            print("Grade D")

result()

