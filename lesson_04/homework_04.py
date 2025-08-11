adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 == +
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

# замінюю "\n" на " "
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 == +
""" Замініть .... на пробіл
"""

# замінюю "...." на " "
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 == +
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

# застосовую цикл із пошуком по подвійним пробілам - поки вони є, будуть замінюватись на одинарний пробіл
while "  " in adwentures_of_tom_sawer:
    adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("  ", " ")

# task 04 +
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

# застосовую цикл із пошуком по символу, додаю в лічильник і виводжу принтом

amount_of_h_symbol = 0

for i in adwentures_of_tom_sawer:
    if i in "h":
        amount_of_h_symbol += 1
    else:
        pass

print(f"amount of (h) symbol inside the text = {amount_of_h_symbol}")

# task 05 +
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

words_with_capital_letter = 0

# розбиваю слова, щоб перевірити перший символ кожного слова
words = adwentures_of_tom_sawer.split()

for i in words:
    # прибираю розділові знаки з початку і кінця кожного слова
    removed_symbols_words = i.strip(".,!?:;\"'()")
    # перевіряю першу літеру кожного слова на велику
    if removed_symbols_words[0].isupper():
        words_with_capital_letter +=1
    else:
        pass

print(f"{words_with_capital_letter} words in the text begin with a capital letter")

# task 06 +
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

# знаходжу індекс першої позиції слова Tom
first_tom_index = adwentures_of_tom_sawer.find("Tom")

# знаходжу індекс другої позиції слова Tom, починаючи з позиції першого індексу
second_tom_index = adwentures_of_tom_sawer.find("Tom", first_tom_index + 1)

print(f"{second_tom_index} is the position where the word Tom is met for second time")


# task 07 +
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = None

# створюю порожній список для речень
sentences_updated = []

# розбиваю речення по крапках, обрізаю пробіли і додаю до списку по циклу

for i in adwentures_of_tom_sawer.split("."):
    if i.strip():
        no_spaces = i.strip()
        sentences_updated.append(no_spaces)
    else:
        pass

adwentures_of_tom_sawer_sentences = sentences_updated
print(adwentures_of_tom_sawer_sentences)

# task 08 +
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print(f"Четверте речення з adwentures_of_tom_sawer_sentences - {adwentures_of_tom_sawer_sentences[3]}")

# перетворюю рядок у нижній регістр
fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print(f"Четверте речення з adwentures_of_tom_sawer_sentences, нижній регістр - {fourth_sentence}")

# task 09 +
""" Перевірте чи починається якесь речення з "By the time".
"""

# проходжусь циклом із пошуком, чи починається рядок зі слів "By the time" і виводжу це речення

for i in adwentures_of_tom_sawer_sentences:
    if i.startswith("By the time"):
        print(f"Речення, що починається з 'By the time':\n{i}")
    else:
        pass

# task 10 +
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

# зберігаю останнє речення в змінну і розбиваю на список слів
last_sentence = adwentures_of_tom_sawer_sentences[-1].split()

# зберігаю кількість слів
words_amount = len(last_sentence)

print(f"Кількість слів останнього речення з adwentures_of_tom_sawer_sentences - {words_amount}")