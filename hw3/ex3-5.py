# 5) Напечатать таблицу умножения для числа n, использовать f строки


def table(n):
    for i in range(1, 11):
        print(f'{n} * {i} = {n * i}')

table(10)