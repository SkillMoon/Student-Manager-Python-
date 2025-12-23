from wsgiref.validate import validator

from student_manager.students import Students
from student_manager.csv_handler import CsvHandler
from student_manager.validator import Validator, ValidatorWithoutRequiredCondition, IDValidatorForMainFunctions


class Manager:
    def __init__(self):
        self.students_list = list()
        CsvHandler().load_from_csv(Students, self.students_list)
    def add_student(self):
        student_id = input("Enter Student ID: ")
        student_id = Validator.validate_id(student_id, self.students_list)
        first_name = input("Enter First Name: ")
        first_name = Validator.validate_name(first_name)
        last_name = input("Enter Last Name: ")
        last_name = Validator.validate_name(last_name)
        age = input("Enter Age: ")
        age = Validator.validate_age(age)
        class_name = input("Enter Class Name: ")
        class_name = Validator.validate_class_name(class_name)
        grade = input("Enter Grade: ")
        grade = Validator.validate_grade(grade)
        self.students_list.append(Students(student_id, first_name, last_name, age, class_name, grade))
        CsvHandler().save_to_csv(self.students_list)
        print('Student added successfully')

    def show_all_students(self):
        print('#' * 20, 'Students', '#' * 20)
        for student in self.students_list:
            print(student)
            print('-' * 15)

    def search_fields(self):
        fields = {
            'student_id': ValidatorWithoutRequiredCondition.validate_id(input('Enter Student ID: ')),
            'first_name': input('Enter First Name: ').lower(),
            'last_name': input('Enter Last Name: ').lower(),
            'age__min':input('Enter Minimum Age: '),
            'age__max': input('Enter Maximum Age: '),
            'age': input('Enter Age: '),
            'class_name': input('Enter Class Name: ').lower(),
            'grade__min': input('Enter Minimum Grade: '),
            'grade__max': input('Enter Maximum Grade: '),
            'grade': input('Enter Grade: ')
        }
        print('*leave fields empty if you dont want to change*')
        accepted_fields = dict()
        for key, value in fields.items():
            if  value:
                accepted_fields[key] = value
        return accepted_fields

    def find_students(self, filters):
        results = self.students_list
        for key, value in filters.items():
            if key.endswith('__min'):
                results = [s for s in results if getattr(s, key[:-5], None) >= value]
            elif key.endswith('__max'):
                results = [s for s in results if getattr(s, key[:-5], None) <= value]
            elif key == 'grade':
                flt_value = float(value)
                results = [s for s in results if getattr(s, key, None).lower() == str(flt_value).lower()]

            else:
                try:
                    results = [s for s in results if getattr(s, key, None).lower() == value]
                except:
                    results = [s for s in results if getattr(s, key, None) == value]
        if results:
            for result in results:
                print(result)
        else:
            print('Student not found')
    def do_search(self):
        return self.find_students(self.search_fields())

    def delete_student(self):
        student_id = IDValidatorForMainFunctions.validate_id(input("Enter student ID to delete: "))
        student = next((s for s in self.students_list if s.student_id == student_id), None)
        if not student:
            print('Student not found')
            return
        confirmation = input(f"Delete {student.first_name} {student.last_name}? (Y/N): ").upper()
        if confirmation != 'Y':
            print("Operation has been cancelled")
        self.students_list.remove(student)
        CsvHandler().save_to_csv(self.students_list)
        print('Student has been deleted')

    def edit_student(self):
        student_id = IDValidatorForMainFunctions.validate_id(input("Enter student ID to edit: "))
        student = next((s for s in self.students_list if s.student_id == student_id), None)
        if not student:
            print('Student not found')
            return
        print(student)
        print('*leave fields empty if you dont want to change*')
        updates = {
            'first_name': ValidatorWithoutRequiredCondition.validate_name(input("Enter First Name: ")),
            'last_name': ValidatorWithoutRequiredCondition.validate_name(input("Enter Last Name: ")),
            'age': ValidatorWithoutRequiredCondition.validate_age(input("Enter Age: ")),
            'class_name': ValidatorWithoutRequiredCondition.validate_class_name(input("Enter Class Name: ")),
            'grade': ValidatorWithoutRequiredCondition.validate_grade(input("Enter Grade: ")),
        }
        for key, value in updates.items():
                if value:
                    setattr(student, key, value)
        CsvHandler().save_to_csv(self.students_list)
        print('Student successfully has been edited')
