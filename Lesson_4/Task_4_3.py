"""Задание 2. Курс Валюты
Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
Код валюты может быть в произвольном регистре.
Функция должна возвращать результат числового типа, например float.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
http://www.cbr.ru/scripts/XML_daily.asp.

Выведите на экран курсы для доллара и евро, используя написанную функцию.

Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере,
посмотреть содержимое ответа."""

import requests
from requests import utils
from decimal import *
from datetime import datetime


def get_currency_rate(currency_code):

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    if 'Date="' in content:
        cutting_edge = content.index('Date="')
        temp_date = content[cutting_edge + 6:cutting_edge + 16].split('.')
        bank_date = datetime(year=int(temp_date[2]), month=int(temp_date[1]), day=int(temp_date[0]))

    if currency_code in content:
        cutting_edge = content.index(user_value)
    else:
        print('None')
        exit(0)

    content = content[cutting_edge:]

    if '<Value>' in content:
        cutting_edge = content.index('<Value>')
    content = content[cutting_edge + 7:cutting_edge + 17].split('<')
    currency = Decimal(float(content[0].replace(',', '.')))  # такое можно делать в одну строку?
    print(f"{user_value} {currency:6.4} {bank_date.strftime('%Y-%m-%d')}")


user_value = str.upper(input('Курс какой валюты нужно отобразить? '))
get_currency_rate(user_value)
