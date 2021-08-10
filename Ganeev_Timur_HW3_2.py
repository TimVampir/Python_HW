# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

# Если делать задание без функции и без звездочки
# key_num = input('Введите число от 0 до 10 на английском: ')
# list_translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
#                   'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
# num_rus = list_translate.get(key_num, None)
# print(num_rus)


def num_translate(key_num):
    """Если делать через функцию задание со звездочкой"""
    list_translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                      'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    num_rus = list_translate.get(key_num.lower(), None)  # если такого ключа нет, выдает None
    if key_num.istitle():
        print(num_rus.capitalize())
    else:
        print(num_rus)


num_translate('one')  # один
num_translate('Eight')  # Восемь
num_translate('Two')  # Два
num_translate('eleven')  # None
