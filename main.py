from samples import *

if __name__ == '__main__':
    create_sample()
    manager.search_student(age__min=15, age__max=18, class_name = 'b1')


