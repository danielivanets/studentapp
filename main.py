import studentcontroller as sc
controllerStudent = sc.StudenController()

#from student import Student

while True:
    print("STUDENT CRUD")
    print("----------------------------")
    print("1.- Add a student")
    print("2.- Delete a student")
    print("3.- Modify a student")
    print("4.- Search a student")
    print("5.- Exit")
    op = int(input("Choose option: "))

    if op == 1:
        print("Addind a new Student")
        dni = input("Enter DNI: ")
        if controllerStudent.searchStudent(dni) is not None:
            print("Oops, DNI already exist.")
            continue
        name = input("Enter Name: ")
        surnames = input("Enter Surnames: ")
        age = int(input("Enter Age: "))
        city = input("Enter City: ")
        province = input("Enter Province: ")
        email = input("Enter Email: ")
        #student = Student(dni, name, surnames, age, city, province, email)
        #self.add_student(student)
        if controllerStudent.addStudent(dni, name, surnames, age, city, province, email):
            print("Student added!")
        else:
            print("Oops, DNI already exist.")
        
    elif op == 2:
        dni = input("Enter DNI to delete: ")
        #self.delete_student(dni)
        if controllerStudent.deleteStudent(dni) is not None:
            print("Student deleted successfully.")
        else:
            print("Student with this DNI not found.")
    elif op == 3:
        dni = input("Enter DNI to modify: ")
        if controllerStudent.searchStudent(dni) is not None:
            print(f"Modification of student with DNI: {dni}")
            print("1.- Modify Name")
            print("2.- Modify Surnames")
            print("3.- Modify Age")
            print("4.- Modify City")
            print("5.- Modify Province")
            print("6.- Modify Email")
            field = int(input("What do you want to modify: "))
            new_value = input("Enter the new value: ")
            if controllerStudent.modifyStudent(dni, field, new_value):
                print("Student modified successfully.")
            else:
                print("Invalid option.")
        else:
            print("Student with this DNI not found.")
    elif op == 4:
        dni = input("Enter DNI to search: ")
        student = controllerStudent.searchStudent(dni)
        if student is not None:
            print(f"Student with DNI: {dni}")
            print(f"Name: {student.get_name()}")
            print(f"Surnames: {student.get_surnames()}")
            print(f"Age: {student.get_age()}")
            print(f"City: {student.get_city()}")
            print(f"Province: {student.get_province()}")
            print(f"Email: {student.get_email()}")
        else:
            print("Student with this DNI not found.")
    elif op == 5:
        print("Exiting...")
        break
    else:
        print("Invalid option. Please choose a valid option.")




"""
class Main(Student):
    def __init__(self):
        Student.__init__(self)
        self.students = {}

    def add_student(self, student):
        if student.get_dni() in self.students:
            print("Student with this DNI already exists.")
        else:
            self.students[student.get_dni()] = student
            print("Student added successfully.")

    def delete_student(self, dni):
        if dni in self.students:
            del self.students[dni]
            print("Student deleted successfully.")
        else:
            print("Student with this DNI not found.")

    def modify_student(self, dni, field, new_value):
        if dni in self.students:
            student = self.students[dni]
            if field == 1:
                student.set_name(new_value)
            elif field == 2:
                student.set_surnames(new_value)
            elif field == 3:
                student.set_age(int(new_value))
            elif field == 4:
                student.set_city(new_value)
            elif field == 5:
                student.set_province(new_value)
            elif field == 6:
                student.set_email(new_value)
            else:
                print("Invalid option.")
            print("Student modified successfully.")
        else:
            print("Student with this DNI not found.")

    def search_student(self, dni):
        if dni in self.students:
            student = self.students[dni]
            print(f"Student with DNI: {dni}")
            print(f"Name: {student.get_name()}")
            print(f"Surnames: {student.get_surnames()}")
            print(f"Age: {student.get_age()}")
            print(f"City: {student.get_city()}")
            print(f"Province: {student.get_province()}")
            print(f"Email: {student.get_email()}")
        else:
            print("Student with this DNI not found.")

"""


"""
    elif option == 3:
        dni = input("Enter DNI to modify: ")
        if dni in self.students:
            print(f"Modification of student with DNI: {dni}")
            print("1.- Modify Name")
            print("2.- Modify Surnames")
            print("3.- Modify Age")
            print("4.- Modify City")
            print("5.- Modify Province")
            print("6.- Modify Email")
            field = int(input("What do you want to modify: "))
            new_value = input("Enter the new value: ")
            self.modify_student(dni, field, new_value)
        else:
            print("Student with this DNI not found.")
    elif option == 4:
        dni = input("Enter DNI to search: ")
        student = controllerStudent.searchStudent(dni)
    

        #self.search_student(dni)
    elif option == 5:
        print("Exiting...")
        break
    else:
        print("Invalid option. Please choose a valid option.")

"""