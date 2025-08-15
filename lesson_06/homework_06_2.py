# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

# створюю змінну для перевірки вводу у циклі

user_input = ""

# перевіряю у циклі, чи містить введене слово 'H' or 'h'
# в умові if переводжу все в нижній регістр

while True:
    user_input = input("Enter any word with 'H' or 'h' symbols:\n")
    if 'h' in user_input.lower():
        print(f"{user_input} word contains required symbols")
        break
    else:
        print(f"{user_input} word does not contain required symbols")