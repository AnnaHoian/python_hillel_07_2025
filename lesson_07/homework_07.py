# task 1 +
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
# def multiplication_table(number):
#     # Initialize the appropriate variable
#     multiplier = 1
#
#     # Complete the while loop condition.
#     while multiplier <= number:
#         result = number * multiplier
#         # десь тут помила, а може не одна
#         if  result > "25":
#             # Enter the action to take if the result is greater than 25
#             pass
#         print(str(number) + "x" + str(multiplier) + "=" + str(result))
#
#         # Increment the appropriate variable
#         multi += 1
#
# multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

def multiplication_table(number):
    # Defined a variable for the multiplier
    multiplier = 1

    # Run the While loop condition while the multiplier is less or equal to 25:
    while multiplier <= 25:
        # Calculated the result of the number and multiplier
        result = number * multiplier
        if  result > 25:
            # Stopped the loop when the result is greater than 25
            break
        else:
            # Printed the multiplication step if the result less than 25
            print(f"{number}x{multiplier}={result}")
            # Incremented the multiplier
            multiplier += 1

# Called a function with 3 as the argument
multiplication_table(3)

# task 2 +
"""  Написати функцію, яка обчислює суму двох чисел.
"""

# Define a function with 2 arguments
def sum_numbers(number1, number2):
    # Return the sum of 2 numbers
    return number1 + number2

# Call a function with 2 numbers entered by a user
sum_result = sum_numbers(int(input("Enter the 1st number:\n")), int(input("Enter the 2nd number:\n")))

print(f"Sum of 2 numbers: {sum_result}")

# task 3 +
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

import random

# Function with generation a list with 10 random numbers in range 1-100

def list_generation():
    # Define a variable for a new list
    random_list = []

    for i in range(10):
        random_number = random.randint(1, 100)
        random_list.append(random_number)
    return random_list

generated_list = list_generation()
print(f"List with numbers: {generated_list}")

def mean_list_number(numbers):
    # Count the number of elements inside the list
    mean_number = len(numbers)

    # Define a variable for a sum
    numbers_sum = 0

    # Sum the numbers in the list
    for number in numbers:
        numbers_sum += number

    # Divide the sum by the number of elements to get the average
    average_number = numbers_sum / mean_number

    return average_number

# Call a function with generated list as a parameter and save the result
mean_number = mean_list_number(generated_list)
print(f"Середнє арифметичне списку чисел = {mean_number}")

# task 4 +
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

# Get text from a user
string_random = input("Enter any text, please:\n")

# Function to reverse a string
def string_reverse(text):
    reverse_string = text[::-1]
    return reverse_string

# Call a function and save the results
reversed_string = string_reverse(string_random)

print(f"String in reverse order:\n{reversed_string}")

# task 5 +
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

# Create a list with random text
text_random= ["Lorem", "ipsum", "dolor", " sit amet", "consectetuer", "adipiscing", "elit"]

# Function to define the longest word
def max_word(words):
    word_greater = max(words, key = len)
    return word_greater

# Save the function result
word_longest = max_word(text_random)

print(f"The longest word in the list is {word_longest}")

# task 6 +
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
# def find_substring(str1, str2):
#
#     return -1

def find_substring(str1, str2):
    # Use searching for substring str2 in string str1:
    # - if the substring is found: returns the index of the first occurrence
    # - if the substring is NOT found: returns -1

    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7 +

# task 05 from HW 3

"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

# Define a function that takes storages values as parameters
def goods(storages, storages1_2, storages2_3):
    # Calculate each storage
    storage3 = storages - storages1_2
    storage1 = storages - storages2_3
    storage2 = storages - (storage3 + storage1)
    # Return storage values in order
    return storage1, storage2, storage3

# Call the function with storages values from the task and save into variables
storage1, storage2, storage3 = goods(375291, 250449, 222950)

print(f"goods in first storage = {storage1}\n"
      f"goods in second storage = {storage2}\n"
      f"goods in third storage = {storage3}")

# task 8 +

# task 6 from HW3

"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

# Define constants for months
ONE_MONTH = 1
YEAR_MONTHS = 12

# Function to calculate the total computer cost
def cost(month_sum, extra_months):
    #Calculate total payment period
    period = YEAR_MONTHS + (ONE_MONTH * extra_months)
    # Calculate total computer cost
    full_sum = month_sum * period
    return full_sum

#Call the function with the task values
computer_cost = cost(1179, 6)

print(f"Computer costs = {computer_cost} UAH")

# task 9 +

# task 9 from HW3

"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

# Function to calculate required number of pages
def album(photos, per_page):
    # Calculate total pages, including extra one
    # to cover the case when some photos do not fill a full page
    pages = (photos + per_page - 1) // per_page
    return pages

# Call the function with task values and save the result
album_pages = album(232, 8)

print(f"Igor will need {album_pages} pages to paste all the photos")


# task 10 +

# task 10 from HW3

"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

# Define a constant for base distance
BASE_KM = 100

# Function to calculate gazoline needs and number of gas stops
def journey_data(cities_distance, base_l, car_reservoir):
    # part 1
    # Calculate total gasoline liters

    full_l = (cities_distance / BASE_KM) * base_l

    # part 2
    # Calculate liters remained after starting with a full reservoir

    first_l = full_l - car_reservoir

    # Calculate the number of gas station visits
    gas_station_stops = int(first_l / car_reservoir)

    if first_l % car_reservoir > 0:
        gas_station_stops += 1

    return full_l, gas_station_stops

# Call a function with task values
full_liters, station_stops = journey_data(1600, 9, 48)

print(f"{full_liters} liters of gasoline will be needed for this trip")
print(f"It will take {station_stops} trips to the gas station.")