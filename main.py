from student_manager.manager import Manager
manager = Manager()
MENU = {
    '1. Add student' : 1, '2. Search student' : 2,
    '3. Delete student' : 3, '4. Edit student' : 4,
    '5. Number of students' : 5, '6. Show all students' : 6,
    '7. Average grades' : 7, '8. Exit' : 8
}
MENU_FUNCTIONS = {
    1 : manager.add_student, 2 : manager.do_search, 3 : manager.delete_student,
    4 : manager.edit_student, 5 : manager.number_of_students, 6 : manager.show_all_students,
    7 : manager.avg_grades, 8 : exit
}
def run():
    for key, op in MENU.items():
        print(key)
    user_input = input('Enter your choice: ')
    if any(char.isalpha() for char in user_input):
        print('Invalid input')
        input('Press ENTER to continue...')
        run()
    user_input = int(user_input)
    if user_input not in MENU_FUNCTIONS.keys():
        print('Invalid input')
        input('Press ENTER to continue...')
        run()
    op = MENU_FUNCTIONS.get(user_input)
    if op:
        op()
        input('Press ENTER to continue...')
        run()
    else:
        pass

if __name__ == '__main__':
    run()

