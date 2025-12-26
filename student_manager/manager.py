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
        if not student_id:
            return
        first_name = input("Enter First Name: ")
        first_name = Validator.validate_name(first_name)
        if not first_name:
            return
        last_name = input("Enter Last Name: ")
        last_name = Validator.validate_name(last_name)
        if not last_name:
            return
        age = input("Enter Age: ")
        age = Validator.validate_age(age)
        if not age:
            return
        class_name = input("Enter Class Name: ")
        class_name = Validator.validate_class_name(class_name)
        if not class_name:
            return
        grade = input("Enter Grade: ")
        grade = Validator.validate_grade(grade)
        if not grade:
            return
        self.students_list.append(Students(student_id, first_name, last_name, age, class_name, grade))
        CsvHandler().save_to_csv(self.students_list)
        print('Student added successfully')

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
                if not any(char.isalpha() for char in value):
                    results = [s for s in results if getattr(s, key[:-5], None) >= value]
                else:
                    results = []
            elif key.endswith('__max'):
                if not any(char.isalpha() for char in value):
                    results = [s for s in results if getattr(s, key[:-5], None) <= value]
                else:
                    results = []
            elif key == 'grade':
                try:
                    flt_value = float(value)
                except:
                    flt_value = str(value)
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
        if not student_id:
            return
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
        if not student_id:
            return
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
        values = []
        for key,value in updates.items():
            values.append(value)
        ValidatorWithoutRequiredCondition.errors = set(ValidatorWithoutRequiredCondition.errors)
        if any(v for v in values if v == 'False'):
            for eror in ValidatorWithoutRequiredCondition.errors:
                print(eror)
            return
        else:
            CsvHandler().save_to_csv(self.students_list)
            print('Student successfully has been edited')

    def show_all_students(self):
        print('*leave field empty if you want to see all students*')
        class_name = ValidatorWithoutRequiredCondition.validate_class_name(input("Enter Class Name: "))
        if class_name:
            print('#' * 20, f'{class_name}\'s Students', '#' * 20)
            for student in self.students_list:
                if student.class_name == class_name:
                    print(student)
        else:
            print('#' * 20, 'Students', '#' * 20)
            for student in self.students_list:
                print(student)
        print('-' * 15)

    def number_of_students(self):
        print('*leave field empty if you want number of students in all classes*')
        class_name = ValidatorWithoutRequiredCondition.validate_class_name(input("Enter Class Name: "))
        count = 0
        if class_name:
            for student in self.students_list:
                if student.class_name == class_name:
                    count += 1
        else:
            count = len(self.students_list)
        if class_name:print(f'*number of {class_name} students*')
        else:print('*number of all students*')
        print('-' * 15)
        print(f'\t{count}')
        print('-' * 15)

    def avg_grades(self):
        print('*leave field empty if you want average of all classes*')
        grades = []
        class_name = ValidatorWithoutRequiredCondition.validate_class_name(input("Enter Class Name: "))
        if class_name:
            for student in self.students_list:
                if student.class_name == class_name:
                    grades.append(float(student.grade))
        else:
            for student in self.students_list:
                grades.append(float(student.grade))
        average = sum(grades) / len(grades)
        if class_name:print(f'*Average Grade of {class_name} students*')
        else:print('*Average Grade of all students*')
        print('-' * 15)
        print(f'\t{average}')
        print('-' * 15)







