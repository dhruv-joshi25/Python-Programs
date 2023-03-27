("""Write a Python Program that creates a student class with appropriate members and 
functions to add student, display student, delete student and search student 
(Use lists or tuple or named tuple, whatever applicable)""")

class Student:
    def __init__(self):
        self.students = {}

    def add_student(self, id, name, age, grade):
        self.students[id] = {'Name': name, 'Age': age, 'Grade': grade}

    def display_student(self, id):
        if id in self.students:
            print("--------------------------")
            print('ID:', id)
            for key, value in self.students[id].items():
                print(key + ':', value)
        else:
            print('Student not found')

    def display_all_student(self):
        for id, student in self.students.items():
            print("--------------------------")
            print('ID:', id)
            for key, value in student.items():
                print(key + ':', value)

    def delete_student(self, id):
        if id in self.students:
            del self.students[id]
            print('Student deleted')
        else:
            print('Student not found')

    def search_student(self, name):
        found = False
        for id, student in self.students.items():
            if student['Name'] == name:
                found = True
                print("--------------------------")
                print('ID:', id)
                for key, value in student.items():
                    print(key + ':', value)
        if not found:
            print('Student not found')

    def write_Record_into_File(self):        
        with open('Student_Records.txt', 'w') as file:
            for id, student in self.students.items():
                file.write('--------------------------\n')
                file.write(f'ID: {id}\n')
                file.write('--------------------------\n')
                for key, value in student.items():
                    file.write(f'{key} : {value}\n')


s = Student()

s.add_student(1, 'Dhruv', 19, 'O')
s.add_student(2, 'Jay', 20, 'A+')
s.add_student(3, 'Dhaval', 21, 'A')
s.add_student(4, 'Anshuman', 21, 'B')
s.add_student(5, 'Shweta', 20, 'B')

print("Enter 1 For Write Record")
print("Enter 2 for Delete record")
print("Enter 3 for Search record")
print("Enter 4 for Display")


choice = int(input("Enter Your choice : "))


if choice == 1:
    s.write_Record_into_File() 
elif choice == 2:
    s.delete_student()
elif choice == 3:
    s.search_student()
elif choice == 4: 
    s.display_all_student()
else:
    print("Invlid Choice!!")