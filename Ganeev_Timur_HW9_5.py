class Stationary:
    title = ''

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationary):
    title = 'Ручка'


class Pencil(Stationary):
    title = 'Карандаш'


class Handle(Stationary):
    title = 'Маркер'


a, b, c = Pen(), Pencil(), Handle()
a.draw(), b.draw(), c.draw()
