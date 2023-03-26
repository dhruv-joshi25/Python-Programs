#Write a Python Program accept comma separated string and 
#display tokens using split(), rsplit() and splitlines()

txt = "This is an example of split(), rsplit(), splitlines()"

print("Orignal text : ",txt)
x = txt.split()
y = txt.rsplit()
z = txt.splitlines()

print("After using split() : ",x)
print("After using rsplit() : ",y)
print("After using splitline() : ",z)