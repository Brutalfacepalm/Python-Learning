# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = False

    def go(self):
        print(f'Автомобиль {self.name} начал движение')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self.name} совершил полицейский разворот {direction}' if self._is_police else f'Автомобиль {self.name} повернул {direction}')

class SportCar:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = False

    def go(self):
        print(f'Автомобиль {self.name} начал движение')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):

        print(f'Автомобиль {self.name} совершил полицейский разворот {direction}' if self._is_police else f'Автомобиль {self.name} повернул {direction}')

class WorkCar:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = False

    def go(self):
        print(f'Автомобиль {self.name} начал движение')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):

        print(f'Автомобиль {self.name} совершил полицейский разворот {direction}' if self._is_police else f'Автомобиль {self.name} повернул {direction}')

class PoliceCar:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = True

    def go(self):
        print(f'Автомобиль {self.name} начал движение')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):

        print(f'Автомобиль {self.name} совершил полицейский разворот {direction}' if self._is_police else f'Автомобиль {self.name} повернул {direction}')

honda = TownCar(210, 'silver', 'Honda Civic')
ferrarri = SportCar(350, 'red', 'Ferrari Laferrari')
bobcat = WorkCar(11, 'white', 'Bobcat S100')
police = PoliceCar(180, 'black', 'NYPD')

honda.go()
ferrarri.go()
bobcat.go()
police.go()

honda.stop()
ferrarri.stop()
bobcat.stop()
police.stop()

honda.turn('влево')
ferrarri.turn('вправо')
bobcat.turn('влево')
police.turn('влево')

