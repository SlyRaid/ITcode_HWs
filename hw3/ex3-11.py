# 11) Напечатать календарь месяца, предполагая, что месяц начинается в понедельник и имеет 31 день

days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

for day in days:
    print(day.center(2), end=' ')
print()

for first in range(1, 8):
    print(str(first).center(2), end=' ')
print()

for second in range(8, 15):
    print(str(second).center(2), end=' ')
print()

for third in range(15, 22):
    print(str(third).center(2), end=' ')
print()

for fourth in range(22, 29):
    print(str(fourth).center(2), end=' ')
print()

for fifth in range(29, 32):
    print(str(fifth).center(2), end=' ')

