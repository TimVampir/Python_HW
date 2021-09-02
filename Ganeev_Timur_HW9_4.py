class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self, direction): # обозначение поворота
        self.direction = direction
        print(f'{self.color} {self.name} повернула на {self.direction}')

    def show_speed(self):
        print(f'Скорость {self.speed}')

    def check_police(self):
        print(f'Полицейская: {self.is_police}')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость: {self.speed}') if self.speed <= 60 else print('Превышена допустимая скорость')

    def check_police(self):
        print(self.is_police)


class SportCar(Car):
    def show_speed(self):
        print(f'Скорость: {self.speed}') if self.speed >= 60 else print(f'Надо бы ускориться')

    def check_police(self):
        print(self.is_police)


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость: {self.speed}') if self.speed <= 40 else print('Превышена допустимая скорость')

    def check_police(self):
        print(self.is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

    def check_police(self):
        print(f'Полицейская {self.is_police}')


c = Car(40, 'Белая', 'Kia')
t = TownCar(50, 'Синяя', 'Honda')
s = SportCar(50, 'Красная', 'Ferrari')
w = WorkCar(40, 'Белая', 'Reno')
p = PoliceCar(80, 'Серая', 'Ford')

s.go(), s.turn('лево'), s.stop()
s.show_speed(), s.check_police()
print(f'Марка авто: {p.name}, Цвет авто: {p.color}, Скорость авто: {p.speed}, Полицейская: {p.is_police}')

