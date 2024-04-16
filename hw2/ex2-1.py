# Запрашиваем строку у пользователя
user_input = input("Введите строку: ")


# 1) Попросите пользователя ввести строку и выведите ее в обратном порядке, не используя метод reverse() и sorted().
def reverse_str(user_input):
    # Создаём пустую строку для хранения символов в обратном порядке
    reversed_string = ""

    # Перебираем символы исходной строки в обратном порядке
    for i in range(len(user_input) - 1, -1, -1):
        reversed_string += user_input[i]

    # Выводим полученную строку в обратном порядке
    print("Обратная строка:", reversed_string)


reverse_str(user_input)
