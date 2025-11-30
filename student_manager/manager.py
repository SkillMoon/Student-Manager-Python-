from student_manager.students import Students

class Manager:
    students_list= list()
    def add_student(self):
        student_id = input("Enter Student ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        age = input("Enter Age: ")
        class_name = input("Enter Class Name: ")
        grade = input("Enter Grade: ")
        self.students_list.append(Students(student_id, first_name, last_name, age, class_name, grade))
