# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements

car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
search_criteria = (2017, 1.6, 36000)

# записую критерії з tuple search_criteria в окремі змінні для фільтрів

criteria_year = search_criteria[0]
criteria_engine = search_criteria[1]
criteria_price = search_criteria[2]

# створюю порожній list для заповнення у циклі

criteria_cars = []

# фільтрую словник, щоб знайти машини згідно search_criteria:
# - рік випуску більше або дорівнює criteria_year
# - об'єм двигуна більше або дорівнює criteria_engine
# - ціна менше або дорівнює criteria_price
# методом .items() повертаю пари ключ-значення
# для цього словника є: ключ - назва авто (Mercedes), значення - tuple з даними ('silver', 2019, 1.8, 'sedan', 50000)
# метод for використовую з ключем у car і значеннями у values ітераторах

for car, values in car_data.items():
    year = values[1] # беру по індексу 1 друге значення (рік) з рядку кожної машини у словнику у tuple
    engine = values[2] # беру по індексу 2 третє значення (об'єм двигуна)
    price = values[4]  # беру по індексу 4 п'яте значення (ціна)

    if year >= criteria_year and engine >= criteria_engine and price <= criteria_price:
        criteria_cars.append((car, values))
        # () - створюю кортеж () і методом .append додаю його до списку, результат - кортеж має усі відсортовані машини

# створюю порожній list для заповнення у циклі

car_price = []

# відбираю лише назву і ціну машини в окремий список

for car in criteria_cars:
    car_price.append([car[0], car[1][4]])
    # створюю список, де буде назва машини і її ціна
    # car[0] - перший елемент tuple (ключ, назва),
    # car[1]- другий елемент (набір значень), [4] - п'ятий субелемент (ціна)


# сортую по другому елементу списку (за зростанням ціни)

car_price.sort(key=lambda i: i[1]) # сортую за ціною (другий елемент)

print("Five first found car elements:")

# виводжу перші знайдені 5 машин

for car in car_price[:5]:
    print(car)