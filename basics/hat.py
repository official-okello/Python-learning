import random

class Hat:
    houses = ['Eden', 'Njura', 'Acem', 'Mwalimu']

    @classmethod
    def sort(cls, name):
        print(name, 'is in', random.choice(cls.houses))

Hat.sort('Julius')