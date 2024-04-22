# 5. Создать базовый класс сотрудник и два дочерних класса – менеджер и работник.
# В базовый класс добавить get_paid(), который в дальнейшем переопределить в дочерних,
# чтобы сотрудники разных должностей получали различную зарплату


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class Manager(Employee):
    def get_paid(self):
        return 50000


class Worker(Employee):
    def get_paid(self):
        return 30000


manager = Manager('Коля', 'Менеджер')
worker = Worker('Толя', 'Работник')

print(f'{manager.name} зарабатывает {manager.get_paid()}₽')
print(f'{worker.name} зарабатывает {worker.get_paid()}₽')
