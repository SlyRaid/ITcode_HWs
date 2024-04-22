# 2. Создать класс “Человек” с полями: имя, город проживания и год рождения.
# Написать метод, который будет возвращать возраст человека в годах
import datetime


class Human():

    def __init__(self, name, city, year_of_birth):
        self.name = name
        self.city = city
        self.year_of_birth = int(year_of_birth)

    def age_in_years(self):
        aiy = datetime.date.today().year
        return aiy - self.year_of_birth


years = Human('Айдар', 'Уфа', '2000')
print(f'Меня зовут {years.name}, я из города {years.city} и мне {years.age_in_years()} года')
