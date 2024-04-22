# 4. Изучить метод __str__, создать класс с данным методом, продемонстрировать его выполнение


class Simple_calc():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Простенький калькулятор'

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


calc = Simple_calc(15, 5)
print(calc.add(), calc.sub(), calc.mult(), calc.div(), sep='\n')
print(calc)
