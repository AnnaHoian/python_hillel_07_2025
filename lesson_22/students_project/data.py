"""
data.py

This module populates the students_project database with initial data.

Function:
    data():
        - Creates courses and students.
        - Adds students to courses randomly.
        - Ensures that no duplicate entries are added if the database
          is already populated.
        - Commits all changes to the database.
        - Logs information about the process.
"""
import logging

from db import SessionLocal, engine
from models import Student, Course, Base
import random

def data():

    Base.metadata.create_all(engine)
    with SessionLocal() as session:

        # Creating courses
        course_programming = Course(name="Python_for_beginners")
        course_db = Course(name="SQL_advance_course")
        course_management = Course(name="PM_introduce")

        session.add_all([course_programming, course_db, course_management])
        session.commit()

        # Creating students
        student1 = Student(name="Anna")
        student2 = Student(name="John")
        student3 = Student(name="Bob")
        student4 = Student(name="Jane")
        student5 = Student(name="Jack")
        student6 = Student(name="Nick")
        student7 = Student(name="Harry")
        student8 = Student(name="Ron")
        student9 = Student(name="Hermione")
        student10 = Student(name="Henry")
        student11 = Student(name="Jim")
        student12 = Student(name="Molly")
        student13 = Student(name="Fred")
        student14 = Student(name="Ginny")
        student15 = Student(name="Tom")

        session.add_all([
            student1, student2, student3, student4, student5, student6, student7,student8,
            student9, student10, student11, student12, student13, student14, student15]
        )
        session.commit()

        # get objects from the database
        courses_in_db = session.query(Course).all()
        students_in_db = session.query(Student).all()

        # Adding students to courses
        students = session.query(Student).all()
        courses = session.query(Course).all()

        for student in students_in_db:
            # random number of courses for each student
            num_courses = random.randint(1, len(courses_in_db))

            # random courses without repetitions
            selected_course = random.sample(courses_in_db, num_courses)

            # add a connection
            student.courses.extend(selected_course)

        session.commit()
        logging.info("Students have been successfully added to random courses")

        for s in students:
            course_titles = [c.name for c in s.courses]
            logging.info(f"{s.name} : {course_titles}")
