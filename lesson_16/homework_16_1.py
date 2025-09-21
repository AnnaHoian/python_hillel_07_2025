"""
Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer,
які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department,
а клас Developer - атрибут programming_language.

Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі атрибути як Manager
(ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді, якою керує
керівник.

Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
"""

class Employee:
    """
    class Employee contains the name and salary values of employee

    Attributes:
    - name (str): Name of the Employee
    - salary (int): Salary of the Employee
    """

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    """
    class Manager contains the department value of manager

    Attributes (Employee inherited):
    - name (str): Name of the Employee
    - salary (int): Salary of the Employee

    Attributes (added):
    - department(str): Department of the manager
    """

    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

class Developer(Employee):
    """
    class Developer contains the programming language value of developer

    Attributes (Employee inherited):
    - name (str): Name of the Employee
    - salary (int): Salary of the Employee

    Attributes (added):
    - programming_language(str): programming language of the developer
    """

    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    """
    class TeamLead contains the team size value of developer

    Attributes (Employee inherited by inheriting Manager and Developer):
    - name (str): Name of the Employee
    - salary (int): Salary of the Employee

    Attributes (Manager inherited):
    - department(str): Department of the manager

    Attributes (Developer inherited):
    - programming_language(str): programming language of the developer

    Attributes (added):
    - team_size(int): employees in the team
    """
    def __init__(self, team_size, **kwargs):
        super().__init__(**kwargs)
        self.team_size = team_size

