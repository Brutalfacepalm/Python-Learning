# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип,
# теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса,
# который наследуется от базового - Игрушка
import time

class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_toy(self):
        print(f'Создана игрушка: {self.name}, {self.color}, {self.type_toy}')


class Toy_animal(Toy):
    def __init__(self, name, color, type_toy):
        super().__init__(name, color)
        self.type_toy = type_toy
        self.make_toy()


class Toy_character(Toy):
    def __init__(self, name, color, type_toy):
        super().__init__(name, color)
        self.type_toy = type_toy
        self.make_toy()

class Make_toy: # класс создания игрушки, сначала производство,
                # в итоге метод new_toy создает класс игрушки и возвращает его экземпляр

    def __init__(self, name, color, type_toy):
        self.name = name
        self.color = color
        self.type_toy = type_toy
        self.purchase()

    def loading(self): # загрузка...
        for i in range(3):
            print('.', end=" ")
            time.sleep(1)

    def purchase(self): # метод закупка сырья, переход к пошиву
        print('Происходит закупка сырья', end=" ")
        self.loading()
        print('\nСырье закуплено')
        self.sewing()

    def sewing(self): # метод пошива, переход к окраске
        print('Пошив игрушки', end=" ")
        self.loading()
        print('\nИгрушка сшита')
        self.painting()

    def painting(self): # метод окраски, переход к выпуску
        print('Покраска игрушки', end=" ")
        self.loading()
        print('\nИгрушка окрашена')
        self.new_toy(self.name, self.color, self.type_toy)

    def new_toy(self, name, color, type_toy): # выпуск игрушки
        if type_toy == 'животное':
            return Toy_animal(name, color, type_toy)
        elif type_toy == 'персонаж мультика':
            return Toy_character(name, color, type_toy)

toy1 = Make_toy('Ослик Иа','серый','персонаж мультика')
toy2 = Make_toy('Енотик','серый','животное')