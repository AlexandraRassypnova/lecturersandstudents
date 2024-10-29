class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.rate_lecturer = {}

    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        # ave_rate = []
        # for grade in self.grades.values():
        #     ave_rate += grade
        # return sum(ave_rate) / len(ave_rate)
        all_grades = sum(self.grades.values(), [])
        return sum(all_grades) / len(all_grades) if all_grades else 0.0

    def __lt__(self, other):
        return self.average_rating() < other.average_rating()

    def __str__(self):
        return (f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние "
                f"задания: {self.average_rating()}\nКурсы в процессе обучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        # ave_rate = []
        # for grade in self.grades.values():
        #     ave_rate += grade
        # return sum(ave_rate) / len(ave_rate)
        all_grades = sum(self.grades.values(), [])
        return sum(all_grades) / len(all_grades) if all_grades else 0.0

    def __lt__(self, other):
        return self.average_rating() < other.average_rating()

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_rating()}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']
best_student_2 = Student('Another', 'Freshman', 'male')
best_student_2.courses_in_progress += ['Python', 'JS']
best_student_2.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('Petr', 'Petrov')
cool_lecturer.courses_attached += ['Python', 'JS']
cool_lecturer_2 = Lecturer('Ivan', 'Ivanov')
cool_lecturer_2.courses_attached += ['JS']
best_student.rate_lecturers(cool_lecturer, 'Python', 10)
best_student.rate_lecturers(cool_lecturer, 'Python', 9)
best_student_2.rate_lecturers(cool_lecturer_2, 'JS', 5)
best_student_2.rate_lecturers(cool_lecturer_2, 'JS', 7)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 4)
cool_reviewer.rate_hw(best_student_2, 'Python', 8)
cool_reviewer.rate_hw(best_student_2, 'Python', 3)
cool_reviewer_2 = Reviewer('One', 'Man')
cool_reviewer_2.courses_attached += ['JS', 'Python']
cool_reviewer_2.rate_hw(best_student, 'JS', 5)
cool_reviewer_2.rate_hw(best_student, 'Python', 2)

print(f"\nРевьюер 1:\n{cool_reviewer}")
print(f"\nРевьюер 2:\n{cool_reviewer_2}")
print(f"\nЛектор 1:\n{cool_lecturer}")
print(f"\nЛектор 2:\n{cool_lecturer_2}")
print(f"\nСтудент 1:\n{best_student}")
print(f"\nСтудент 2:\n{best_student_2}")
print(f"\nСредняя оценка студента 1 {best_student.average_rating()}")
print(f"Средняя оценка студента 2 {best_student_2.average_rating()}")
print(f'У второго студента средняя оценка больше? {best_student<best_student_2}')
print(f"\nСредняя оценка лектора 1 {cool_lecturer.average_rating()}")
print(f"Средняя оценка лектора 2 {cool_lecturer_2.average_rating()}")
print(f'У первого лектора средняя оценка больше? {cool_lecturer_2<cool_lecturer}')

students = [best_student, best_student_2]
course = 'Python'
# def average_rating_student_course(students: list[Student], course):
#     ave = []
#     for m in students:
#         ave.extend(m.grades.get(course, []))
#     return  f'\nСредняя оценка среди студентов по курсу {course} : {sum(ave)/len(ave)}'
def average_rating_student_course(students, course):
    grades = [grade for student in students for grade in student.grades.get(course, [])]
    return f"\nСредняя оценка среди студентов по курсу {course}: {sum(grades)/len(grades):.2f}" if grades else "Нет оценок."
print(average_rating_student_course(students, course))

lectory = [cool_lecturer, cool_lecturer_2]
course_l = 'JS'
# def average_rating_lecturers_course(lectory: list[Lecturer], course_l):
#     aver = []
#     for m in lectory:
#         aver.extend(m.grades.get(course_l, []))
#     return  f'\nСредняя оценка среди лекторов по курсу {course_l} : {sum(aver)/len(aver)}'
def average_rating_lecturers_course(lecturers, course):
    grades = [grade for lecturer in lecturers for grade in lecturer.grades.get(course, [])]
    return f"\nСредняя оценка среди лекторов по курсу {course}: {sum(grades)/len(grades):.2f}" if grades else "Нет оценок."
print(average_rating_lecturers_course(lectory, course_l))
