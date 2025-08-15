# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

# створюю порожній список
lst2 = []

# перебираю lst1 за наявності рядків і записую їх у новий список

for str_data in lst1:
    if isinstance(str_data, str):
        lst2.append(str_data)

print(f"New list with only string values:\n{lst2}")