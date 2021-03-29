""""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
выбросить исключение ValueError. Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
...
raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
"""

import re

RE_EMAIL = re.compile(r'(.+)@(.+)')
parse_result = {'username': '1', 'domain': '2'}


def email_parse(email_adress):
    x = RE_EMAIL.findall(email_adress)[0]
    parse_result['username'] = x[0]
    parse_result['domain'] = x[1]


email_parse('araimo@yandex.ru')
print(parse_result)
