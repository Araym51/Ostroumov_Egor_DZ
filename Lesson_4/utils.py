
import requests
from requests import utils
from decimal import *
from datetime import datetime


def get_currency_rate(currency_code):
    """

    :param currency_code:
    :return:
    """
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    if 'Date="' in content:
        cutting_edge = content.index('Date="')
        temp_date = content[cutting_edge + 6:cutting_edge + 16].split('.')
        bank_date = datetime(year=int(temp_date[2]), month=int(temp_date[1]), day=int(temp_date[0]))

    currency_code = str.upper(currency_code)

    if currency_code in content:
        cutting_edge = content.index(currency_code)
        content = content[cutting_edge:]

        if '<Value>' in content:
            cutting_edge = content.index('<Value>')
        content = content[cutting_edge + 7:cutting_edge + 17].split('<')
        currency = Decimal(float(content[0].replace(',', '.')))
        print(f"{currency_code} {currency:6.4} {bank_date.strftime('%Y-%m-%d')}")

    else:
        print('None')
        exit(0)


def get_currency_rate_terminal(currency_code):

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    if 'Date="' in content:
        cutting_edge = content.index('Date="')
        temp_date = content[cutting_edge + 6:cutting_edge + 16].split('.')
        bank_date = datetime(year=int(temp_date[2]), month=int(temp_date[1]), day=int(temp_date[0]))

    currency_code = str.upper(currency_code[1])
    """
    с помощью print обнаружил,аргументы из терминала передаются списком:
    python utils.py usd через терминал приобретают вид ['utils', usd]
    """

    if currency_code in content:
        cutting_edge = content.index(currency_code)
        content = content[cutting_edge:]

        if '<Value>' in content:
            cutting_edge = content.index('<Value>')
        content = content[cutting_edge + 7:cutting_edge + 17].split('<')
        currency = Decimal(float(content[0].replace(',', '.')))
        print(f"{currency_code} {currency:6.4} {bank_date.strftime('%Y-%m-%d')}")

    else:
        print('None')
        exit(0)
