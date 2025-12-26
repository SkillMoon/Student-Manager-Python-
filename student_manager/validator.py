class Validator:
    @staticmethod
    def validate_id(student_id, students_list):
        if student_id.strip() == "":
            print("Student ID is required")
            return
        try:
            student_id = int(student_id)
        except ValueError:
            print("Student ID is not a number")
            return
        for student in students_list:
            if student.student_id == student_id:
                print("student id already exists")
                return
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
            return
        for char in ban_chars:
            if char in name:
                print("cant use numbers and signs in name")
                return
        return name

    @staticmethod
    def validate_age(age):
        age = age.strip()
        if not age:
            print("Age is required")
            return
        try:
            age = int(age)
        except ValueError:
            print("Age is not a number")
            return
        if age not in range(16,20):
            print("Age must be between 16 and 19")
            return
        return age

    @staticmethod
    def validate_class_name(class_name):
        class_name = class_name.strip().lower()
        if not class_name:
            print("Class name is required")
            return
        return class_name

    @staticmethod
    def validate_grade(grade):
        grade = grade.strip()
        if not grade:
            print("Grade is required")
            return
        try:
            grade = float(grade)
        except ValueError:
            print("Grade is not a number")
            return
        if grade not in range(0,21):
            print("Grade is not between 0 and 20")
            return
        return grade

#valide values for edit and search : because in edit and search variables can be empty
class ValidatorWithoutRequiredCondition:
    errors = []
    @staticmethod
    def validate_id(student_id):
        try:
            student_id = int(student_id)
        except:
            student_id = str(student_id)
        return student_id
    @staticmethod
    def validate_name(name):
        name = name.strip()
        ban_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#',
                     '$', '%', '^', '&', '*', '(', ')', '_', '-''+', '=', '[', ']',
                     '{', '}', ';', ':', '\'', '\"', '|', '/', '\\', '?', '.', ',',
                     '<', '>']
        for char in ban_chars:
            if char in name:
                ValidatorWithoutRequiredCondition.errors.append("cant use numbers and signs in name")
                name = 'False'
        return name
    @staticmethod
    def validate_age(age):
        age = age.strip()
        if age:
            try:
                age = int(age)
            except ValueError:
                ValidatorWithoutRequiredCondition.errors.append("Age is not a number")
                age = 'False'
            if age not in range(16, 20) and age != 'False':
                ValidatorWithoutRequiredCondition.errors.append("Age is not between 16 and 19")
                age = 'False'
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
                ValidatorWithoutRequiredCondition.errors.append("Grade is not a number")
                grade = 'False'
            if grade not in range(0, 21) and grade != 'False':
                ValidatorWithoutRequiredCondition.errors.append("Grades is not between 0 and 20")
                grade = 'False'
        return grade
#validate student id in main fields(delete,edit)
class IDValidatorForMainFunctions:
    @staticmethod
    def validate_id(student_id):
        if student_id.strip() == "":
            print("Student ID is required")
            return
        try:
            student_id = int(student_id)
        except ValueError:
            print("Student ID is not a number")
            return
        return student_id