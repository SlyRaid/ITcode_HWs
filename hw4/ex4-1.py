# 1. Создать класс для геометрической фигуры на выбор и добавить в него два метода – первый
# для расчета площади, второй для расчета периметра


class Kvadrat():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square_fig(self):
        square = self.a * self.b
        return square

    def perimeter_fig(self):
        perimeter = 2 * self.a + 2 * self.b
        return perimeter


gf = Kvadrat(a=5, b=2)
print(gf.square_fig())
print(gf.perimeter_fig())
