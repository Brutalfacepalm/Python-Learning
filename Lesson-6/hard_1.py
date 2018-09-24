# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.
import time

class Toy:
    def __init__(self, name, color, type_toy):
        self.name = name
        self.color = color
        self.type_toy = type_toy
        self.make_toy()

    def make_toy(self):
        print(f'Создана игрушка: {self.name}, {self.color}, {self.type_toy}')

class Make_toy: # класс создания игрушки, сначала производство,
                # в итоге метод new_toy создает нвоый класс Toy и возвращает его экземпляр

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
        return Toy(name, color, type_toy)

toy1 = Make_toy('Ослик Иа','серый','персонаж мультика')
toy2 = Make_toy('Енотик','серый','животное')