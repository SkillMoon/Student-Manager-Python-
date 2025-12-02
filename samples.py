from student_manager.manager import Manager
from student_manager.students import Students
def create_sample():
    s1 = Students(
        student_id='12', first_name="John", last_name="Smith", age=18,
        class_name='b1', grade=20
        )
    s2 = Students(
        student_id='13', first_name="matin", last_name="salesi", age=19,
        class_name='b1', grade=18
        )
    s3 = Students(
        student_id='14', first_name="ali", last_name="ahmadi", age=21,
        class_name='b2', grade=16
    )
    Manager().students_list.append(s1)
    Manager().students_list.append(s2)
    Manager().students_list.append(s3)
manager = Manager()