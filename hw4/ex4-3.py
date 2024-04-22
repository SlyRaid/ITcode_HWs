# 3. Создать класс калькулятор и описать в нём методы для базовых математических операций для двух чисел


class Simple_calc():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        if self.b == 0:
            return 'На 0 делить нельзя'
        return self.a / self.b


calc = Simple_calc(15, 5)
print(calc.add(), calc.sub(), calc.mult(), calc.div(), sep='\n')
