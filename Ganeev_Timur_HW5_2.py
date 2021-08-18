n = input('Введите максимальное значение: ')
max_num = int(n)

nums_gen = (num for num in range(1, max_num + 1, 2))
print(*nums_gen)