"""
main.py
Represents the Student-Course project:
    1. Populates database with initial data
    2. Queries students and courses
    3. Updates student and course names
    4. Deletes students and courses
"""
import logging
from data import data
from operations import (
    get_students_by_course,
    get_courses_by_student,
    update_course_name,
    update_student_name,
    delete_student
)
from db import session
from models import Student, Course
from pathlib import Path

# log file configurations
log_dir = Path(__file__).parent
log_file = log_dir / 'student_project_log.log'

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    # 1. Fill database with students and courses data
    data()

    # 2. Student and course queries
    get_students_by_course("Python_for_beginners")
    get_courses_by_student("Anna")

    # 3. Update student and course
    student = session.query(Student).filter_by(name="Anna").first()
    course = session.query(Course).filter_by(name="Python_for_beginners").first()

    if student:
        update_student_name(str(student.id), "Alice")

    if course:
        update_course_name(str(course.id), "Ruby_for_beginners")

    # 4. Delete a student
    deleted_student = session.query(Student).order_by(Student.id.desc()).first()

    if deleted_student:
        delete_student(str(deleted_student.id))

if __name__ == "__main__":
    main()

