"""
This file contains previous homework functions, which were covered by unittests
"""

"""
Task 05 from HW 3 +

Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

def goods(storages, storages1_2, storages2_3):
    """
    Function goods calculate goods in each storage by difference from existing storages data
    """

    storage3 = storages - storages1_2
    storage1 = storages - storages2_3
    storage2 = storages - (storage3 + storage1)

    return storage1, storage2, storage3

storage1, storage2, storage3 = goods(375291, 250449, 222950)

"""
Task 4 from HW7 +

Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

string_random = "text"

def string_reverse(text):
    """
    Function string_reverse takes an existing string and returns it in reverse order
    """
    reverse_string = text[::-1]
    return reverse_string

reversed_string = string_reverse(string_random)

"""
Task 9 from HW3 +

Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

def album(photos, per_page):
    """
    Function album calculates required number of pages, including extra one
    to cover the case when some photos do not fill a full page
    """
    pages = (photos + per_page - 1) // per_page
    return pages

album_pages = album(232, 8)

"""
Task 3 from HW 6 +

Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
Дані в лісті можуть бути будь якими
"""

def list_with_strings(lst1):
    """
    Function list_with_strings fills in a new list with only string data from entry list
    """
    lst2 = []
    for str_data in lst1:
        if isinstance(str_data, str):
            lst2.append(str_data)
    return lst2

new_strings_list = list_with_strings(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])

