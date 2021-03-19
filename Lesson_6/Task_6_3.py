"""3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и
формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать,
что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи"""

import json

file_hobby = open('hobby.csv', 'r', encoding='utf-8')
file_users = open('users.csv', 'r', encoding='utf-8')
result_dict = {}
line_user = file_users.readline()
line_hobby = file_hobby.readline()

while line_user:
    result_dict.setdefault(line_user, line_hobby)   # Никак не мог додуматься как читать  два файла одновременно.
    line_user = file_users.readline()               # озарение было внезапным.
    line_hobby = file_hobby.readline()

file_hobby.close()
file_users.close()

with open('result_Task_6_3.csv', 'a', encoding='utf-') as file_result:
    converter = json.dumps(result_dict)
    file_result.write(converter)
