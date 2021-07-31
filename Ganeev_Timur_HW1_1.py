time = int(input('Введите продолжительность в секундах: '))
hour = time // 3600
minute = time // 60 % 60
second = time % 60
print(hour, 'час', minute, 'мин', second, 'cек')