# 4) Выведите количество слов в строке, не используя метод split()


# Запрашиваем строку у пользователя
user_input = input("Введите строку: ")


def count_words(user_input):
    count = 0
    word = False
    for char in user_input:
        if char.isalpha() and not word:
            count += 1
            word = True
        elif not char.isalpha():
            word = False
    print("Количество слов:", count)


count_words(user_input)
