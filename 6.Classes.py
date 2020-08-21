import random
class main:
    deliver_value = 0 #собранное количество яиц,молока,шерсти
    graze = False #маркер выгула
    # feed = ''
    # voice = ''
    counter = 0
    def walk(self):
        self.graze = True
        # self.counter = 100 * hour / 12 #сколько погуляли столько и дали яиц,молока,шерсти
        print(f'{self.name} прогуляла и скушала {self.feed}')

    def voice_(self):
        print(f'кричит {self.voice}')

class animals(main):
    horns = True
    feed = 'hay'

    def take_deliver(self):
        # if self.graze == True:
            self.deliver_value = random.uniform(1.0, 10.0)
        # else:
        #     print('Сначала нужно выгулять и покормить')

class birds(main):
    wings = True
    delivery = 'egg'

    def take_deliver(self):
        # if self.graze == True:
        self.deliver_value = random.randint(1, 5)
        # else:
        #     print('Сначала нужно выгулять и покормить')
        print(f'{self.name} снесла яйца в количестве - {self.deliver_value} штук')

# животные  - корова, козы и овцы
class cow(animals):
    name = 'Manya'
    delivery = 'milk'
    voice = 'moooo'
    weight = 36
    def take_deliver(self):
        super().take_deliver()
        print(f'{self.name} дала - {round(self.deliver_value,2)} литров {self.delivery}')

class goat_horns(animals):
    name = 'goat_horns'
    delivery = 'milk'
    voice = 'bee'
    species = 'horns'
    weight = 31
    def take_deliver(self):
        super().take_deliver()
        print(f'{self.name} дала - {round(self.deliver_value,2)} литров {self.delivery}')

class goat_hooves(goat_horns):
    name = 'goat_hooves'
    species = 'hooves'
    weight = 39

class sheep_barash(animals):
    name = 'sheep_barash'
    delivery = 'wool'
    voice = 'bkheee'
    species = 'barashek'
    weight = 53
    def take_deliver(self):
        super().take_deliver()
        print(f'с {self.name} состригли {round(self.deliver_value,2)} килограмм {self.delivery}')

class sheep_kydrya(sheep_barash):
    name = 'sheep_kydrya'
    species = 'kydrya'
    weight = 48

# птицы - гуси, курицы и утки
class goose_white(birds):
    name = 'goose_white'
    feed = 'roots'
    voice = 'ga-ga-ga'
    color = 'white'
    weight = 3.3

class goose_gray(goose_white):
    name = 'goose_gray'
    color = 'gray'
    weight = 2.5

class chicken_koko(birds):
    name = 'chicken_koko'
    feed = 'millet'
    voice = 'ko-ko-ko'
    weight = 0.85

class chicken_kykareky(chicken_koko):
    name = 'chicken_kykareky'
    voice = 'ky-ka-re-ky'
    weight = 0.93

class duck(birds):
    name = 'Kryakva'
    feed = 'corn'
    voice = 'krya-krya'
    weight = 1.23

weights = {'cow': cow.weight, 'goat_horns': goat_horns.weight, 'sheep_barash': sheep_barash.weight,
             'sheep_kydrya': sheep_kydrya.weight, 'goose_white': goose_white.weight,
             'goose_gray': goose_gray.weight, 'chicken_koko': chicken_koko.weight,
             'chicken_kykareky': chicken_kykareky.weight, 'duck': duck.weight}
def feed_all():
    cow.walk(cow)
    cow.voice_(cow)
    goat_horns.walk(goat_horns)
    goat_horns.voice_(goat_horns)
    goat_hooves.walk(goat_hooves)
    goat_hooves.voice_(goat_hooves)
    sheep_barash.walk(sheep_barash)
    sheep_barash.voice_(sheep_barash)
    sheep_kydrya.walk(sheep_kydrya)
    sheep_kydrya.voice_(sheep_kydrya)
    goose_white.walk(goose_white)
    goose_white.voice_(goose_white)
    goose_gray.walk(goose_gray)
    goose_gray.voice_(goose_gray)
    chicken_koko.walk(chicken_koko)
    chicken_koko.voice_(chicken_koko)
    chicken_kykareky.walk(chicken_kykareky)
    chicken_kykareky.voice_(chicken_kykareky)
    duck.walk(duck)
    duck.voice_(duck)
def take_food():
    cow().take_deliver()
    goat_horns().take_deliver()
    goat_hooves().take_deliver()
    sheep_barash().take_deliver()
    sheep_kydrya().take_deliver()
    goose_white().take_deliver()
    goose_gray().take_deliver()
    chicken_koko().take_deliver()
    chicken_kykareky().take_deliver()
    duck().take_deliver()
def max_weight():
    return print(f'Максимальный вес у {max(weights, key=weights.get)} - {max(weights.values())} кг')
def summ_weights():
    summ = 0
    for elem in weights.values():
        summ += elem
    print(f'общий вес всех обитателей = {summ} кг')
def main_request():
    while True:
        requests_dict = {
            'feed': feed_all,
            'food': take_food,
            'max': max_weight,
            'summ': summ_weights,
            'e': exit}
        user_input = input(
            'Введите команду:\nfeed - покормить\nfood - собрать\nmax - узнать максимальный вес\nsumm - узнать обий вес обитателей\ne - exit\n')
        requests_dict[user_input]()
    print('До свидания')
main_request()


def main_request():
    requests_animal_bird = {
            'animal': {
                'cow': cow
                'goat': {
                    'horns': goat_horns
                    'hooves': goat_hooves
                    }
                'sheep': {
                    'barash': sheep_barash
                    'kydrya': sheep_kydrya
                    }
            }
            'bird': {
                'goose': {
                    'white': goose_white
                    'gray': goose_gray
                    }
                'chicken': {
                    'koko': chicken_koko
                    'kykareky': chicken_kykareky
                    }
                'duck': duck
            }
        }
        requests_dict = {
            'walk': 'Погулять',
            'deviver': 'Собрать',
            'sum': 'Общий вес',
            'max': 'Максимальный вес',
            'e': exit}
        user_input_0 = input('Введите команду:\nanimal - животное (корова, козы и овцы)\n'
                             'bird - птицы (гуси, курицы и утки)')
        if user_input_0 == 'animal':
            user_input_animal = input('Выберите животное:\ncow - корова\ngoat - коза\nsheep - овца')
        if user_input_animal == 'goat':
            user_input_goat = input('Какой породы козы:\nhorns - рога\nhooves - копыта')
            if user_input_goat == 'horns'

            else:

        else:
            user_input_bird = input('Выберите птицу:\ngoose - гусь\nchicken - курица\nduck - утка')
            if user_input_animal == 'goat':
                user_input_goat = input('Какого цвета гуси:\nwhite - белые\ngray - серые')
                if user_input_goat == 'white'

                else:
        requests_animal_bird[user_input_0]()
        user_input_1 = input('Введите команду:\nwalk - чтобы выгулять\ndeliver - чтобы собрать\n'
                           'sum - показать общий вес\nmax - показать максимальный вес\ne - exit\n')
        requests_dict[user_input_1]()
    print('До свидания')
