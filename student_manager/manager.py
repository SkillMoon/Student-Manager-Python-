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
    def show_all_students(self):
        print('#' * 20, 'Students', '#' * 20)
        for student in self.students_list:
            print(student)
            print('-' * 15)


    def search_student(self, **filters):
        results = self.students_list
        for key, value in filters.items():
            if key.endswith('__min'):
                results = [s for s in results if getattr(s, key[:-5], None) >= value]
            elif key.endswith('__max'):
                results = [s for s in results if getattr(s, key[:-5], None) <= value]
            else:
                results = [s for s in results if getattr(s, key, None) == value]
        if results:
            for result in results:
                print(result)
        else:
            print('Student not found')

    def delete_student(self):
        student_id = input("Enter student ID to delete: ")
        student = next((s for s in self.students_list if s.student_id == student_id), None)
        if not student:
            print('Student not found')
            return
        confirmation = input(f"Delete {student.first_name} {student.last_name}? (Y/N): ").upper()
        if confirmation != 'Y':
            print("Operation has been cancelled")
        self.students_list.remove(student)
        print('Student has been deleted')