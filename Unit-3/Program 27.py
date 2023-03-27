("""Write a program to read any text file line by line""")

file1 = open("C:\8029\Python/file1.txt", "r")

read_content = file1.readlines()
print(read_content)
file1.close()