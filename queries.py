"""
LINQ-запити варіанту 2 у двох стилях.

У Python немає двох синтаксисів LINQ, тому застосовано відповідність:
  * «синтаксис запитів»  -> декларативні вирази-генератори / comprehension;
  * «синтаксис методів»  -> функціональний стиль: filter, map, min, Counter + lambda.
"""
from collections import Counter

from models import Course, Student

COURSE_TITLE = "Programming Basics"
MAX_AGE = 20


# ---------- Запит 1: студенти до 20 років на курсі "Programming Basics" ----------

def q1_query(students: list[Student], courses: list[Course]) -> list[Student]:
    course_ids = {c.id for c in courses if c.title == COURSE_TITLE}
    return [s for s in students if s.age < MAX_AGE and s.course_id in course_ids]


def q1_method(students: list[Student], courses: list[Course]) -> list[Student]:
    course_ids = set(map(lambda c: c.id, filter(lambda c: c.title == COURSE_TITLE, courses)))
    return list(filter(lambda s: s.age < MAX_AGE and s.course_id in course_ids, students))


# ---------- Запит 2: join студентів із курсами (ім'я студента, назва курсу) ----------

def q2_query(students: list[Student], courses: list[Course]) -> list[tuple[str, str]]:
    by_id = {c.id: c for c in courses}  # hash join
    return [(s.name, by_id[s.course_id].title) for s in students if s.course_id in by_id]


def q2_method(students: list[Student], courses: list[Course]) -> list[tuple[str, str]]:
    by_id = dict(map(lambda c: (c.id, c), courses))
    matched = filter(lambda s: s.course_id in by_id, students)
    return list(map(lambda s: (s.name, by_id[s.course_id].title), matched))


# ---------- Запит 3: кількість студентів на кожному курсі ----------

def q3_query(students: list[Student], courses: list[Course]) -> list[tuple[str, int]]:
    counts = Counter(s.course_id for s in students)
    return [(c.title, counts.get(c.id, 0)) for c in courses]


def q3_method(students: list[Student], courses: list[Course]) -> list[tuple[str, int]]:
    counts = Counter(map(lambda s: s.course_id, students))
    return list(map(lambda c: (c.title, counts.get(c.id, 0)), courses))


# ---------- Запит 4: наймолодший студент ----------

def q4_query(students: list[Student], courses: list[Course]) -> Student:
    min_age = min(s.age for s in students)
    return next(s for s in students if s.age == min_age)


def q4_method(students: list[Student], courses: list[Course]) -> Student:
    return min(students, key=lambda s: s.age)


# ---------- Неефективні варіанти (для порівняння продуктивності) ----------

def q2_nested_loop_join(students: list[Student], courses: list[Course]) -> list[tuple[str, str]]:
    """Join вкладеними циклами: O(n * m)."""
    return [(s.name, c.title) for s in students for c in courses if s.course_id == c.id]


def q3_count_per_course_naive(students: list[Student], courses: list[Course]) -> list[tuple[str, int]]:
    """Підрахунок окремим проходом по студентах для кожного курсу: O(n * m)."""
    return [(c.title, sum(1 for s in students if s.course_id == c.id)) for c in courses]


def q4_sorted_first(students: list[Student], courses: list[Course]) -> Student:
    """Сортування лише заради першого елемента: O(n log n) замість O(n)."""
    return sorted(students, key=lambda s: s.age)[0]
