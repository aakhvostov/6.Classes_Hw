import random
random.randint(1, 40)
random.uniform(1.0, 19.9)

class Creature:
    dict_of_creatures = {}
    noise = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Creature.dict_of_creatures[self.name] = self.weight

    def go_to_walk(self):
        print(f'{self.name} had walked')

    def make_a_noise(self):
        print(f'{self.name} says {self.noise}!')

    def feed(self):
        print(f'{self.name} eating - "om-nom-nom!"')

    # def get_dict_of_creatures(self):
    #     Creature.dict_of_creatures[self.name] = self.weight


class Bird(Creature):
    def get_eggs(self):
        print('eggs collected')


class MilkyWay(Creature):
    def get_milk(self):
        print('milk taken')


class Cow(MilkyWay):
    creature_type = 'Корова'
    noise = 'Мууу-ууу-ууу'


class Goat(MilkyWay):
    creature_type = 'Козочка'
    noise = 'Мее-еее-еее'

    def __init__(self, name, weight, special):
        super().__init__(name, weight)
        self.special = special


class Sheep(Creature):
    creature_type = 'Овечка'
    noise = 'Бее-еее-еее'

    def __init__(self, name, weight, wool_type):
        super().__init__(name, weight)
        self.wool_type = wool_type

    def get_wool(self):
        print(f'wool {self.wool_type} collected')


class Goose(Bird):
    creature_type = 'Гуси'
    noise = 'Га-га-га'

    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color


class Chicken(Bird):
    creature_type = 'Курица'

    def __init__(self, name, weight, noise):
        super().__init__(name, weight)
        self.noise = noise


class Duck(Bird):
    creature_type = 'Утка'
    noise = 'Кря-кря-кря'


# dori = Duck('Dori', 4)
# dori.get_dict_of_creatures()
# dori.feed()
# print(Creature.__dict__)
# kiri = Goose('Kiri', 15, 'White')
# kiri.get_dict_of_creatures()
# kiri.feed()
# print(f'{kiri.name} is {kiri.color}')
# print(Creature.__dict__)
# koko = Chicken('Sel', 2, 'Kykareky')
# koko.get_dict_of_creatures()
# koko.make_a_noise()
# koko.feed()
# print(Creature.dict_of_creatures)


def get_creatures():
    cow = Cow('Маня', random.randint(20, 50))
    goat1 = Goat('Варечка', random.randint(12, 19), 'рога')
    goat2 = Goat('Cарочка', random.randint(12, 19), 'копыта')
    sheep1 = Sheep('Маруся', random.randint(15, 30), 'бараш')
    sheep2 = Sheep('Алиса', random.randint(15, 30), 'кудряш')
    goose1 = Goose('Саня', random.randint(9, 17), 'белый')
    goose2 = Goose('Даня', random.randint(9, 17), 'серый')
    chick1 = Chicken('Кокошка', round(random.uniform(1.0, 9.9), 2), 'Ко-ко-ко')
    chick2 = Chicken('Кукарешка', round(random.uniform(1.0, 9.9), 2), 'Ку-ка-реку')
    duck = Duck('Донни', random.randint(10, 23))


get_creatures()


def get_max_weight():
    print(f'Максимальный вес у {max(Creature.dict_of_creatures, key=Creature.dict_of_creatures.get)} - '
          f'{max(Creature.dict_of_creatures.values())} кг')


get_max_weight()


def get_summ_of_weight():
    print(f'общий вес всех созданий - {sum(Creature.dict_of_creatures.values())} кг')


get_summ_of_weight()