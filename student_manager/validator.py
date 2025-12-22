class Validator:
    @staticmethod
    def validate_id(student_id, students_list):
        if student_id.strip() == "":
            print("Student ID is required")
            exit()
        try:
            student_id = int(student_id)
        except ValueError:
            print("Student ID is not a number")
            exit()
        for student in students_list:
            if student.student_id == student_id:
                print("student id already exists")
                exit()
        return student_id
    @staticmethod
    def validate_name(name):
        name = name.strip()
        ban_chars = ['1','2','3','4','5','6','7','8','9','0','!','@','#',
                     '$','%','^','&','*','(',')','_','-''+','=','[',']',
                     '{','}',';',':','\'','\"','|','/','\\','?','.',',',
                     '<','>']
        if not name:
            print("Name is required")
            exit()
        for char in ban_chars:
            if char in name:
                print("cant use numbers and signs in name")
                exit()
        return name

    @staticmethod
    def validate_age(age):
        age = age.strip()
        if not age:
            print("Age is required")
            exit()
        try:
            age = int(age)
        except ValueError:
            print("Age is not a number")
            exit()
        if age not in range(16,20):
            print("Age must be between 16 and 19")
            exit()
        return age

    @staticmethod
    def validate_class_name(class_name):
        class_name = class_name.strip().lower()
        if not class_name:
            print("Class name is required")
            exit()
        return class_name

    @staticmethod
    def validate_grade(grade):
        grade = grade.strip()
        if not grade:
            print("Grade is required")
            exit()
        try:
            grade = float(grade)
        except ValueError:
            print("Grade is not a number")
            exit()
        if grade not in range(0,21):
            print("Grade is not between 0 and 20")
            exit()
        return grade

#valide values for edit : because in edit variables can be empty
class ValidatorForEdit():
    @staticmethod
    def validate_name(name):
        name = name.strip()
        ban_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#',
                     '$', '%', '^', '&', '*', '(', ')', '_', '-''+', '=', '[', ']',
                     '{', '}', ';', ':', '\'', '\"', '|', '/', '\\', '?', '.', ',',
                     '<', '>']
        for char in ban_chars:
            if char in name:
                print("cant use numbers and signs in name")
                exit()
        return name
    @staticmethod
    def validate_age(age):
        age = age.strip()
        if age:
            try:
                age = int(age)
            except ValueError:
                print("Age is not a number")
                exit()
            if age not in range(16, 20):
                print("Age must be between 16 and 19")
                exit()
        return age
    @staticmethod
    def validate_class_name(class_name):
        class_name = class_name.lower().strip()
        return class_name
    @staticmethod
    def validate_grade(grade):
        grade = grade.strip()
        if grade:
            try:
                grade = float(grade)
            except ValueError:
                print("Grade is not a number")
                exit()
            if grade not in range(0, 21):
                print("Grade is not between 0 and 20")
                exit()
        return grade
#validate student id in main fields(delete,search,edit)
class ValidatorForMainFunctions():
    @staticmethod
    def validate_id(student_id):
        if student_id.strip() == "":
            print("Student ID is required")
            exit()
        try:
            student_id = int(student_id)
        except ValueError:
            print("Student ID is not a number")
            exit()
        return student_id