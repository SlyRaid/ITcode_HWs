# 2) Замените в пользовательской строке все появления буквы h на букву H, кроме первого и последнего вхождения.


# Запрашиваем строку у пользователя
user_input = input("Введите строку: ")


def hHh(user_input):
    # Создаём копию исходной строки для работы с ней
    copy_string = user_input

    # Создаём новую строку, в которой заменим все 'h' на 'H', кроме первого и последнего
    new_string = (copy_string[:copy_string.find('h') + 1] +
                  copy_string[copy_string.find('h') + 1:copy_string.rfind('h')].replace('h', 'H') +
                  copy_string[copy_string.rfind('h'):])

    # Выводим результат
    print("Новая строка:", new_string)


hHh(user_input)
