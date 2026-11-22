import random

from models import Course, Student


def create_courses() -> list[Course]:
    return [
        Course(1, "Programming Basics", 6),
        Course(2, "Databases", 5),
        Course(3, "Web Development", 6),
        Course(4, "Algorithms", 5),
        Course(5, "Networks", 4),
        Course(6, "Operating Systems", 5),
        Course(7, "Mathematics", 4),
        Course(8, "English", 3),
        Course(9, "Cybersecurity", 5),
        Course(10, "UI/UX Design", 3),
    ]


def create_students() -> list[Student]:
    return [
        Student(1, "Олександр Мельник", 18, 1),
        Student(2, "Марія Коваленко", 19, 1),
        Student(3, "Іван Бондаренко", 21, 1),
        Student(4, "Софія Шевченко", 17, 2),
        Student(5, "Андрій Ткачук", 22, 2),
        Student(6, "Анна Кравченко", 20, 3),
        Student(7, "Дмитро Олійник", 19, 1),
        Student(8, "Катерина Поліщук", 23, 4),
        Student(9, "Максим Лисенко", 18, 3),
        Student(10, "Юлія Мороз", 24, 5),
        Student(11, "Богдан Савчук", 19, 6),
        Student(12, "Оксана Рудюк", 20, 7),
        Student(13, "Тарас Гончар", 21, 8),
        Student(14, "Вікторія Клименко", 18, 9),
        Student(15, "Павло Яремчук", 22, 4),
        Student(16, "Ірина Левченко", 19, 3),
        Student(17, "Назар Петренко", 20, 1),
        Student(18, "Олена Васильєва", 21, 10),
        Student(19, "Денис Бойко", 17, 6),
        Student(20, "Таміла Гриценко", 23, 2),
    ]


def create_large_data(students_count: int, courses_count: int) -> tuple[list[Student], list[Course]]:
    """Згенерований великий набір даних для порівняння продуктивності."""
    rng = random.Random(42)
    courses = [Course(i, f"Course {i}", rng.randint(3, 6)) for i in range(1, courses_count + 1)]
    courses[0] = Course(1, "Programming Basics", 6)
    students = [
        Student(i, f"Student {i}", rng.randint(17, 30), rng.randint(1, courses_count))
        for i in range(1, students_count + 1)
    ]
    return students, courses
