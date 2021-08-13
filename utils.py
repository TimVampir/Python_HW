import re
import sys
from requests import get

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
xml_str = response.text
xml_str = xml_str.replace('<Value>', '(')
xml_str = xml_str.replace('</Value>', ')')
xml_str = xml_str.replace('(специальные права заимствования)', ' ')
# форматируем текст в удобный формат

course = re.findall(r"[(](.+?)[)]", xml_str)    # извлекаем курс валют
idx = re.findall('[A-Z]{3}', xml_str)   # извлекаем названия валют

dict_course = dict(zip(idx, course))    # создаем словарь


def currency_rates(key):
    """Поиск курса валюты по ключу"""
    meaning = dict_course.get(key)
    print(f'Курс валюты {key} равен: {meaning}')


if __name__ == '__main__':
    exit(currency_rates(sys.argv[1]))
# из консоли тоже все работает
