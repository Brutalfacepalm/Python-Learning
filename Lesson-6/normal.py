# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def dps(self, armor_enemy):
        return self.damage / armor_enemy


class Player(Person):

    def __init__(self, health, damage, armor, name):
        super().__init__(health, damage, armor)
        self.name = name

    def attack(self, health_enemy, armor_enemy):
        health_enemy -= self.dps(armor_enemy)
        return health_enemy

class Enemy(Person):

    def __init__(self, health, damage, armor, name):
        super().__init__(health, damage, armor)
        self.name = name

    def attack(self, health_player, armor_player):
        health_player -= self.dps(armor_player)
        return health_player

class Battle:

    def __init__(self, player, enemy):
        self.pl_nm = player.name
        self.en_nm = enemy.name
        self.pl_hp = player.health
        self.en_hp = enemy.health
        self.pl_arm = player.armor
        self.en_arm = enemy.armor
        self.pl_dmg = player.dps(enemy.armor)
        self.en_dmg = enemy.dps(player.armor)
        self.count = 0
        self.start(player, enemy)

    def start(self, player, enemy):
       while True:
            self.en_hp = player.attack(self.en_hp, self.en_arm)
            self.count += 1
            self._hit(self.count, self.pl_nm, self.en_nm, self.pl_dmg, self.en_hp)
            if self.en_hp > 0:
                self.pl_hp = enemy.attack(self.pl_hp, self.pl_arm)
                self.count += 1
                self._hit(self.count, self.en_nm, self.pl_nm, self.en_dmg, self.pl_hp)
                if self.pl_hp < 0:
                    self._win(self.en_nm, self.en_hp)
                    break
            else:
                self._win(self.pl_nm, self.pl_hp)
                break
    def _win(self, winner, hp):
        print(f'Победил {winner}, у него соталось {int(round(hp,0))} HP.')

    def _hit(self, count, attacking_name, attacked_name, attacking_damage, attacked_health):
        print('{} удар. {} атаковал {}, нанеся ему {} единиц урона и оставив {} HP'
              .format(count, attacking_name, attacked_name, int(round(attacking_damage,0)), int(round(attacked_health,0))))


pl = Player(150, 20, 1.3, 'Bob')
en = Enemy(100, 30, 1.3, 'John')
mk = Battle(pl, en)