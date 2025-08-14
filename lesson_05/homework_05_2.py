# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13 have age >=30.
# Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# 1. створюю власний запис (tuple)
my_record = ('Anna', 'Lee', 25, 'Data Analyst', 'France')

# додаю my record на початок списку (0)

people_records.insert(0, my_record)

# 2. обмінюю елементи 1 і 5 у people_records місцями

people_records[1], people_records[5] = people_records[5], people_records[1]
print(f"Modified list with swapped elements with indexes 1 and 5 (1<->5): \n{people_records}")

# w. проходжусь по записам з індексом [6, 10, 13] і перевіряю чи їм 30 років або більше

for i in [6, 10, 13]:
    person = people_records[i] # дістаю tuple зі списку
    if person[2] >= 30:
        print(f"{person[0]} {person[1]} is 30 or older")
    else:
        print(f"{person[0]} {person[1]} is not 30 or older")
