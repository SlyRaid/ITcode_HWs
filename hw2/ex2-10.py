def check_unique(sequence):
    sequence = list(sequence)  # Преобразуем последовательность в список для удобства работы
    for num in sequence:
        if sequence.count(num) > 1:  # Проверяем, сколько раз число встречается в списке
            return False  # Если число повторяется, возвращаем False
        return True  # Если все числа уникальны, возвращаем True


# Пример использования функции
sequence = [1, 1, 3, 4, 5, 6, 7, 8, 9]
print(check_unique(sequence))  # Выведет True, если все числа уникальны
