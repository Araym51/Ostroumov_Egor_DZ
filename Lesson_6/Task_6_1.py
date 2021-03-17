"""
1. Не используя библиотеки для парсинга, распарсить
(получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

file_1 = open('nginx_logs.txt', 'r', encoding='utf-8')
file_2 = open('result.txt', 'a', encoding='utf-8')

for line in file_1:
    temp = line.split()
    remover = str(temp[5]).replace('"', '')
    txt = f'{temp[0]} {remover} {temp[6]}\n '
    file_2.write(txt)

file_1.close()
file_2.close()

"""
Без with open программа отрабатывает мгновенно.
Ну и неудачное решение, на которое мой ПК тратил 15-20 сек:
"""
# with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
#     for line in file_1:
#         temp = line.split()
#         txt = f'{temp[0]} {temp[5]} {temp[6]}\n '
#
#         with open('oatmeal.txt', 'a', encoding='utf-8') as f:
#             f.write(txt)
