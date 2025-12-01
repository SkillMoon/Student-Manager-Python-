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
        print('#' * 50)

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