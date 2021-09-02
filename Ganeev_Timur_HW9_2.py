class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def count_mass(self, layer):
        print(f'Масса дороги {int((layer * self._lenght * self._width * 25) / 1000)} т.')

my_road = Road(5000, 20)
my_road.count_mass(5)