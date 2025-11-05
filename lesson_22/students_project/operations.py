"""
operations.py contains:
    Database Queries:
        returns information about students registered for a particular course
        returns information the courses for which a particular student is registered

    Update and Delete Data:
        updating student and course data
        deleting a student from the database
"""
import logging

from db import session
from models import Student, Course


def get_students_by_course(course_name: str):

    course = session.query(Course).filter_by(name=course_name).first()
    if not course:
        logging.warning(f"Course {course_name} is not found")
        return
    for student in course.students:
        logging.info(f"{student.name} has been registered for a {course_name} course")

def get_courses_by_student(student_name: str):

    student = session.query(Student).filter_by(name=student_name).first()
    if not student:
        logging.warning(f"Student {student_name} not found")
        return
    for course in student.courses:
        logging.info(f"{student_name} has been registered for a {course.name} course")

def update_student_name(student_id: str, new_name: str):
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        logging.warning(f"Student {student_id} is not found")
        return
    old_name = student.name
    student.name = new_name
    session.commit()
    logging.info(f"Student {student_id} has been updated from {old_name} to {new_name}")

def update_course_name(course_id: str, new_name: str):
    course = session.query(Course).filter_by(id=course_id).first()
    if not course:
        logging.warning(f"Course {course_id} is not found")
        return
    old_name = course.name
    course.name = new_name
    session.commit()
    logging.info(f"Course {course_id} has been updated from {old_name} to {new_name}")

def delete_student(student_id: str):
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        logging.warning(f"Student {student_id} is not found")
        return
    session.delete(student)
    session.commit()
    logging.info(f"Student {student_id} has been deleted")



