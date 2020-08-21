class Creature:
    noice = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def go_to_walk(self):
        print(f'{self.name} had walked')

    def make_a_noice(self):
        print(f'{self.name} says {noice}!')

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
    noice = 'Мууу-ууу-ууу'


class Goat(MilkyWay):
    creature_type = 'Козочка'
    noice = 'Мее-еее-еее'

    def __init__(self, special):
        super().__init__()
        self.special = special


class Sheep(Creature):
    creature_type = 'Овечка'
    noice = 'Бее-еее-еее'

    def __init__(self, wool_type):
        self.wool_type = wool_type
        super().__init__()

    def get_wool(self):
        print(f'wool {self.wool_type} collected')


class Goose(Bird):
    creature_type = 'Гуси'
    noice = 'Га-га-га'

    def __init__(self, color):
        super().__init__(name, weight)
        self.color = color


class Chicken(Bird):
    creature_type = 'Курица'

    def __init__(self, noice):
        super().__init__()
        self.noice = noice


class Duck(Bird):
    creature_type = 'Утка'
    noice = 'Кря-кря-кря'


dori = Duck('Dori', 10)
dori.feed()

kiri = Goose('Kiri', 15, 'White')