"""
models.py

This module contains:
    a description of which tables will be in the database.
    specified columns, types, and relationships between tables.
    prepared structure for further adding students and courses.
"""

import uuid
from typing import List
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    """Base class for all models."""
    pass

# Many-to-many associative table for students and courses
student_course = Table(
    'student_course',
    Base.metadata,
    Column('student_id', UUID(as_uuid=True), ForeignKey("students.id"), primary_key=True),
    Column('course_id', UUID(as_uuid=True), ForeignKey("courses.id"), primary_key=True)
)

class Student(Base):
    """
    Student model.

    Attributes:
        id (UUID): Unique student identifier.
        name (str): Student name.
        courses (List[Course]): Courses the student is enrolled in.
    """

    __tablename__ = 'students'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    courses: Mapped[List["Course"]] = relationship(
        "Course",
        secondary=student_course,
        back_populates="students")

    def __repr__(self):
        return f'<id = {self.id} and name = {self.name}>'

class Course(Base):
    """
    Course model.

    Attributes:
        id (UUID): Unique identifier for the course.
        name (str): Course name.
        students (List[Student]): Students enrolled in the course.
    """

    __tablename__ = 'courses'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    students: Mapped[List["Student"]] = relationship(
        'Student',
        secondary=student_course,
        back_populates='courses')

    def __repr__(self):
        return f'<id = {self.id} and name = {self.name}>'

