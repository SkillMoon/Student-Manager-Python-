class Students:
    def __init__(self, student_id, first_name, last_name, age, class_name, grade):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.class_name = class_name
        self.grade = grade

    def __str__(self):
        return (f'std id : {self.student_id}, name : {self.first_name} { self.last_name}'
                f', class : {self.class_name}, age : {self.age}, grade: {self.grade}')
