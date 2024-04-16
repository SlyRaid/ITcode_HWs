# 3) Выведите количество слов в строке


# Запрашиваем строку у пользователя
user_input = input("Введите строку: ")


def word_count(user_input):
    # Разделяем строку на слова и считаем их количество
    words = user_input.split()
    w_c = len(words)

    # Выводим результат
    print("Количество слов:", w_c)


word_count(user_input)
