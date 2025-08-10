# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

# task 01 +

alice_in_wonderland = ("Would you tell me, please, which way I ought to go from here?\n"
                       "That depends a good deal on where you want to get to," " - said the Cat.\n"
                       "I don't much care where" " - said Alice.\n"
                       "Then it doesn't matter which way you go," " - said the Cat.\n"
                       "—— so long as I get somewhere," " - Alice added as an explanation.\n"
                       "Oh, you're sure to do that," " - said the Cat," " - if you only walk long enough.")

# task 02 +

amount_of_symbol = 0
for i in alice_in_wonderland:
    if i in "'":
        print(f"(') symbol = {i}")
        amount_of_symbol += 1
    else:
        pass

print(f"amount of (') symbol inside the variable = {amount_of_symbol}")

# task 03 +

print(alice_in_wonderland)

# Доброго дня! Я не впевнена, що зрозуміла правильно це завдання, тож зробила його наступним чином:
# task1 - виправила текст і відобразила у фізичні лінії по аналогії з діалогом (мова персонажу - наступний рядок)
# task2 - вивела в консоль усі (') символи і їх кількість (розумію, що мало б бути рішення іншим чином, але не здогадалась...)
# task3 - вивела в консоль виправлену змінну з task1

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04 +
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

area_black_sea = 436402
area_azov_sea = 37800

area_of_two_sea = area_black_sea + area_azov_sea
print(f"Area of both seas = {area_of_two_sea} km²")


# task 05 +
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

goods_all = 375291
goods_1and2_storages = 250449
goods_2and3_storages = 222950

goods_3storage = goods_all - goods_1and2_storages
goods_1storage = goods_all - goods_2and3_storages
goods_2storage = goods_all - (goods_3storage + goods_1storage)

print(f"goods in first storage = {goods_1storage}\n"
      f"goods in second storage = {goods_2storage}\n"
      f"goods in third storage = {goods_3storage}")

# task 06 +
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
payment_sum_in_month = 1179
year_months = 12
one_month = 1
payment_period = year_months + (one_month * 6)
computer_cost = payment_sum_in_month * payment_period

print(f"Computer costs = {computer_cost} UAH")


# task 07 +
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

remainder_a = 8019 % 8
remainder_b = 9907 % 9
remainder_c = 2789 % 5
remainder_d = 7248 % 6
remainder_e = 7128 % 5
remainder_f = 19224 % 9

# task 08 +
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_large_sum = 4
pizza_large_amount = 274
pizza_large_order = pizza_large_sum * pizza_large_amount

pizza_middle_sum = 2
pizza_middle_amount = 218
pizza_middle_order = pizza_middle_sum * pizza_middle_amount

juice_sum = 4
juice_amount = 35
juice_order = juice_sum * juice_amount

cake_sum = 1
cake_amount = 350
cake_order = cake_sum * cake_amount

water_sum = 3
water_amount = 21
water_order = water_sum * water_amount

order_full = pizza_large_order + pizza_middle_order + juice_order + cake_order + water_order

print(f"Amount of Irinka`s order is = {order_full} UAH")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photos_all = 232
photos_per_page = 8
pages = (photos_all + photos_per_page - 1) // photos_per_page
# added (photos_per_page - 1) to be sure if no photos left out of full pages
# (in this case, Igor will require an extra page)

print(f"Igor will need {pages} pages to paste all the photos")

# task 10 +
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
cities_distance = 1600
base_km = 100
base_l = 9
car_reservoir = 48

# 1. Скільки літрів бензину знадобиться для такої подорожі?

full_l = (cities_distance / base_km) * base_l

print(f"{full_l} liters of gasoline will be needed for this trip")

# 2. Скільки щонайменше разів родині необхідно заїхати на заправку під час цієї подорожі,
# кожного разу заправляючи повний бак?

# Рахується, скільки потрібно буде літрів взагалом на дорогу, якщо сім'я вирушила з повним баком

first_l = full_l - car_reservoir

# Рахується кількість заїздів на заправку

gas_station_stops = int(first_l / car_reservoir)

# Перевіряємо, чи немає залишків від ділення (якщо так - потрібна ще зупинка)
if first_l % car_reservoir > 0:
    gas_station_stops +=1
else:
    pass

print(f"It will take {gas_station_stops} trips to the gas station.")