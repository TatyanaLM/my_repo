"""Создание класса "Студент" с атрибутами "имя", "фамилия", "курс", "средний балл".
Реализовать методы для добавления и удаления студента, изменения данных студента,
вывода информации о всех студентах, а также поиска студента по фамилии."""


# импортируем класс
class Student:
    def __init__(self, name, sname, course, score):
            self.name = name
            self.sname = sname
            self.course = course
            self.score = score
            Student._students = []

    def add_student(cls, student):
        cls.students.append(student)

    def change_course(self, course):
        self.course = course

    def print_students(self):
            for student in self.students:
                print(f'{student.name} {student.sname}, course: {student.course}, score: {student.score}')

    def search_student(self, sname):
            for student in self.students:
                if student.sname == sname:
                    print(f'{student.name} {student.sname}, course: {student.course}, score: {student.score}')
            else:
                print("Студент не найден!")

# создаем объекты студентов
student1 = Student("Иван", "Иванов", 1, 4.5)
student2 = Student("Петр", "Петров", 2, 3.7)

# добавляем студента
student3 = Student("Сергей", "Сергеев", 1, 4.0)
Student.add_student(student3)

# изменяем данные студента
student1.change_course(4)

# выводим информацию о всех студентах
student1.print_students()

# ищем студента по фамилии
student1.search_student("Петрова")