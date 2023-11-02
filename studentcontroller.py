import student as st
class StudenController():
    def __init__(self):
        self.__students = {}

    def addStudent(self, dni, name, surnames, age, city, province, email):
        if dni not in self.__students:
            student = st.Student(dni, name, surnames, age, city, province, email)
            self.__students[dni] = student
            return True
        return False
    
    def deleteStudent(self,dni):
        if dni in self.__students:
            student = self.__students.pop(dni)
            return student
        return None
    
    def searchStudent(self,dni):
        #if dni in self.__students.keys["dni"]:
        if dni in self.__students:
            student = self.__students[dni]
            return student
        return None

    def modifyStudent(self,dni,field,new_value):
        student = self.__students[dni]
        if field == 1:
           student.set_name(new_value)
        elif field == 2:
            student.set_surnames(new_value)
        elif field == 3:
            student.set_age(new_value)
        elif field == 4:
            student.set_city(new_value)
        elif field == 5:
            student.set_province(new_value)
        elif field == 6:
            student.set_email(new_value)
        else:
            return False
        return True

