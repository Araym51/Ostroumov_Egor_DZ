# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10
# c английского на русский язык. Например:
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.

voccabulary = {'zero': 'ноль',
               'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять'}


userText = str(input('Какое числительное от 0 до 10 требуется перевести с английского на русский?'))


def num_translate(word):
    """ функция выводит все значения по переданному ключу """
    print(voccabulary.get(word))

num_translate(userText)

# Лучше хранить в словарях. Легче искать - по ключам.
# В теле функции в данной задаче лучше использовать текстовый вид данных из-за данных в словаре.
