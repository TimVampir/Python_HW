cube = []
sum_digits = 0
for numbers in range(1, 1000, 2):
    cube.append(numbers ** 3)
for numbers in cube:
    sum_number = 0
    numbers_second = numbers
    while numbers_second > 0:
        number = numbers_second % 10
        sum_number += number
        numbers_second = numbers_second // 10
    if sum_number % 7 == 0:
        sum_digits += numbers
print(sum_digits)
sum_digits = 0
for numbers in cube:
    sum_number = 0
    numbers_second = numbers + 17
    while numbers_second > 0:
        number = numbers_second % 10
        sum_number += number
        numbers_second = numbers_second // 10
    if sum_number % 7 == 0:
        sum_digits += numbers + 17
print(sum_digits)