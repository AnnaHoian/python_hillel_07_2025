"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". Створіть об'єкт цього класу,
представляючи студента. Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""

class Student:
    """
    class Student contains data about a student and changes their middle score

    Attributes:
    name (str) - student name
    surname (str) - student surname
    middle_score (int) - student middle score
    age (int) - student age

    Methods:
    change_score(new_score):
     - verifies that student middle score in 1-100 range
     - updates the middle score
     - prints a message with a new score/error
    """

    def __init__(self, name, surname, middle_score, **kwargs):
        self.name = name
        self.surname = surname
        self.middle_score = middle_score
        self.age = kwargs.get('age')

    def change_score(self, new_score):
        self.middle_score = new_score
        if new_score > 0:
            if new_score <= 100:
                print(f"New student {self.name} middle score is {new_score}")
            else:
                print(f"Error: score must be between 1 and 100")
        else:
            print(f"Error: score must be between 1 and 100")

student_data = Student("Anna", "Doe", 90, age=25)
student_data.change_score(95)

