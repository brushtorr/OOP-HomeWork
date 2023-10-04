import re


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Метод для выставления оценки за лекцию
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.lecture_in_progress:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [grade]
            else:
                lecturer.lecture_grades[course] = [grade]
        else:
            return 'Ошибка'

    # Метод для расчета средней оценки за домашние задания
    def calculate_average_grade(self):
        total_grades = 0
        total_courses = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_courses += len(grades)
        return round(total_grades / total_courses, 1) if total_courses > 0 else 0

    # Метод для отображения информации о студенте
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {(self.calculate_average_grade)()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    # Перегрузка операторов сравнения для студентов
    def __lt__(self, other):
        return self.calculate_average_grade() < other.calculate_average_grade()

    def __le__(self, other):
        return self.calculate_average_grade() <= other.calculate_average_grade()

    def __gt__(self, other):
        return self.calculate_average_grade() > other.calculate_average_grade()

    def __ge__(self, other):
        return self.calculate_average_grade() >= other.calculate_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    # Метод для отображения информации о наставнике
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_in_progress = []
        self.lecture_grades = {}

    # Метод для расчета средней оценки за лекции
    def calculate_average_grade(self):
        total_grades = 0
        total_courses = 0
        for grades in self.lecture_grades.values():
            total_grades += sum(grades)
            total_courses += len(grades)
        return round(total_grades / total_courses, 1) if total_courses > 0 else 0

    # Метод для отображения информации о лекторе
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.calculate_average_grade()}')

    # Перегрузка операторов сравнения для лекторов
    def __lt__(self, other):
        return self.calculate_average_grade() < other.calculate_average_grade()

    def __le__(self, other):
        return self.calculate_average_grade() <= other.calculate_average_grade()

    def __gt__(self, other):
        return self.calculate_average_grade() > other.calculate_average_grade()

    def __ge__(self, other):
        return self.calculate_average_grade() >= other.calculate_average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Метод для выставления оценки за домашнее задание студенту
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Метод для отображения информации о проверяющем
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


# Функция для расчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def calculate_average_hw_grade(students, course_name):
    total_grades = 0
    total_students = 0
    for student in students:
        if course_name in student.grades:
            total_grades += sum(student.grades[course_name])
            total_students += len(student.grades[course_name])
    return round(total_grades / total_students, 1) if total_students > 0 else 0


# Функция для расчета средней оценки за лекции всех лекторов в рамках курса
def calculate_average_lecture_grade(lecturers, course_name):
    total_grades = 0
    total_lecturers = 0
    for lecturer in lecturers:
        if course_name in lecturer.lecture_grades:
            total_grades += sum(lecturer.lecture_grades[course_name])
            total_lecturers += len(lecturer.lecture_grades[course_name])
    return round(total_grades / total_lecturers, 1) if total_lecturers > 0 else 0


# Создаем объекты
best_student = Student('Влад', 'Буторин')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Анатолий', 'Воркутинский')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 9.9)
cool_reviewer.rate_hw(best_student, 'Python', 9.9)
cool_reviewer.rate_hw(best_student, 'Python', 9.9)

best_lecturer = Lecturer('Владимир', 'Пупкин')
best_lecturer.lecture_in_progress += ['Python']

best_student.rate_lecture(best_lecturer, 'Python', 9.9)
best_student.rate_lecture(best_lecturer, 'Python', 9.9)
best_student.rate_lecture(best_lecturer, 'Python', 9.9)

# Сравнение студентов и лекторов
student1 = Student('Student1', 'Surname1')
student1.courses_in_progress += ['Python']
student1.grades['Python'] = [9.9, 9.9, 9.9]

student2 = Student('Student2', 'Surname2')
student2.courses_in_progress += ['Git']
student2.grades['Python'] = [9.9, 9.9, 9.9]

lecturer1 = Lecturer('Lecturer1', 'Surname1')
lecturer1.lecture_in_progress += ['Python']
lecturer1.lecture_grades['Python'] = [9.9, 9.9, 9.9]

lecturer2 = Lecturer('Lecturer2', 'Surname2')
lecturer2.lecture_in_progress += ['Git']
lecturer2.lecture_grades['Python'] = [9.9, 9.9, 9.9]

# Создаем список студентов и лекторов
students = [best_student, student1, student2]
lecturers = [best_lecturer, lecturer1, lecturer2]

# Вызываем функции для расчета средних оценок
course_name = 'Python'
average_hw_grade = calculate_average_hw_grade(students, course_name)
average_lecture_grade = calculate_average_lecture_grade(lecturers, course_name)

# Вывод информации
print(cool_reviewer)
print()
print(best_lecturer)
print()
print(best_student)
print()
print(student1 <= student2)
print(student1 >= student2)
print(lecturer1 >= lecturer2)
print(lecturer1 <= lecturer2)
print(student1 < student2)
print(student1 > student2)
print(lecturer1 > lecturer2)
print(lecturer1 < lecturer2)
print()
print(f"Средняя оценка за домашние задания по курсу {course_name}: {average_hw_grade}")
print(f"Средняя оценка за лекции по курсу {course_name}: {average_lecture_grade}")
