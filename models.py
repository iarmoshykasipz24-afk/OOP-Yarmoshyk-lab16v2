from dataclasses import dataclass


@dataclass(frozen=True)
class Course:
    id: int
    title: str
    credits: int


@dataclass(frozen=True)
class Student:
    id: int
    name: str
    age: int
    course_id: int
