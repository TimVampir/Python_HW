from itertools import zip_longest, islice


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Виктор'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

# rez = zip_longest(tutors, klasses, fillvalue=None) # Если без генератора
rez = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses, fillvalue=None))  # C генератором
print(*islice(rez, len(tutors)), sep='\n')
