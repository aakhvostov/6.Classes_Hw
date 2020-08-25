import random


class Creature:
    dict_of_creatures = {}
    dict_of_weight = {}
    noise = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Creature.dict_of_weight[self.name] = self.weight

    def go_to_walk(self):
        print(f'{self.name} had walked')

    def make_a_noise(self):
        print(f'{self.name} says {self.noise}!')

    def feed(self):
        print(f'{self.name} eating - "om-nom-nom!"')


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


list_of_creatures = []
cow = Cow('Буренка', random.randint(20, 50))
list_of_creatures.append(cow)
goat1 = Goat('Варечка', random.randint(12, 23), 'рога')
list_of_creatures.append(goat1)
goat2 = Goat('Маня', random.randint(12, 23), 'копыта')
list_of_creatures.append(goat2)
sheep1 = Sheep('Маруся', random.randint(15, 30), 'бараш')
list_of_creatures.append(sheep1)
sheep2 = Sheep('Алиса', random.randint(15, 30), 'кудряш')
list_of_creatures.append(sheep2)
goose1 = Goose('Саня', random.randint(9, 17), 'белый')
list_of_creatures.append(goose1)
goose2 = Goose('Даня', random.randint(9, 17), 'серый')
list_of_creatures.append(goose2)
chick1 = Chicken('Кокошка', round(random.uniform(1.0, 9.9), 2), 'Ко-ко-ко')
list_of_creatures.append(chick1)
chick2 = Chicken('Кукарешка', round(random.uniform(1.0, 9.9), 2), 'Ку-ка-реку')
list_of_creatures.append(chick2)
duck = Duck('Донни', random.randint(10, 23))
list_of_creatures.append(duck)


def get_max_weight():
    print(f'Максимальный вес у {max(Creature.dict_of_weight, key=Creature.dict_of_weight.get)} - '
          f'{max(Creature.dict_of_weight.values())} кг')


def get_sum_of_weight():
    print(f'общий вес всех созданий - {sum(Creature.dict_of_weight.values())} кг')


get_max_weight()
get_sum_of_weight()

for elem in list_of_creatures:
    print()
    elem.go_to_walk()
    elem.feed()
    elem.make_a_noise()
    if isinstance(elem, MilkyWay):
        elem.get_milk()
    elif isinstance(elem, Bird):
        elem.get_eggs()
    elif isinstance(elem, Sheep):
        elem.get_wool()
