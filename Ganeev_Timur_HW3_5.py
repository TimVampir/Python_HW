# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
# (по одному из каждого)
from random import randint


def get_jokes(n):
    """Функция для вызова другой функции n раз"""
    for i in range(n):
        fun()


def fun():
    """Функция создания шуток"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    first_word = nouns[randint(0, len(nouns) - 1)]
    second_word = adverbs[randint(0, len(adverbs) - 1)]
    third_word = adjectives[randint(0, len(adjectives) - 1)]
    joke = [first_word, second_word, third_word]
    print(joke)


get_jokes(3)   # 3 - количество шуток
