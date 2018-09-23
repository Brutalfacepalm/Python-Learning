# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'Автомобиль {self.name} начал движение')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self.name} совершил полицейский разворот {direction}' if self._is_police else f'Автомобиль {self.name} повернул {direction}')


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = False

class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = False

class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = False

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = True

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
police.turn('вправо')