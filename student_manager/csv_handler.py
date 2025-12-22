from csv import DictReader, DictWriter


class CsvHandler:

    @staticmethod
    def load_from_csv(cls, students_list):
        try:
            with open('data/students.csv', newline='') as csvfile:
                rows = DictReader(csvfile)
                for row in rows:
                    students_list.append(
                    cls(
                        int(row['student_id']),
                        row['first_name'],
                        row['last_name'],
                        row['age'],
                        row['class_name'],
                        row['grade']
                    )
                    )
        except Exception as e:
            print(e)
            with open('data/students.csv', 'w', newline='') as csvfile:
                headers = ["student_id", "first_name", "last_name", "age", "class_name", "grade"]
                writer = DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()

    @staticmethod
    def save_to_csv(students_list):
        with open('data/students.csv', 'w', newline='') as csvfile:
            headers = ["student_id", "first_name", "last_name", "age", "class_name", "grade"]
            writer = DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for student in students_list:
                writer.writerow(student.__dict__)