# Задание 4
# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран
# фразы вида: 'Привет, Игорь!
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

word_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
newList = []

for b in word_list:
    newList = newList + b.split(" ")

print('Привет,', newList[1], '!')
print('Привет,', newList[4].capitalize(), '!')
print('Привет,', newList[8].capitalize(), '!')
print('Привет,', newList[10].capitalize(), '!')

# после создания pull request посмотрю как решали Вы, и сделаю выводы.
# самому не очень нравится решение.