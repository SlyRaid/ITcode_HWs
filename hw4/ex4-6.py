# 6. * Изучить что такое множественное наследование и миксины, привести пример использования данных концепций ООП


class Mixin:
    def get_info(self):
        print(f"Формат {self.__class__.__name__} - {self.format}")

class foto_1:
    format = "jpg"

class foto_2:
    format = "png"

class Pokazfoto_1(foto_1, Mixin):
    pass

class Pokazfoto_2(foto_2, Mixin):
    pass

video = Pokazfoto_1()
video.get_info()

audio = Pokazfoto_2()
audio.get_info()