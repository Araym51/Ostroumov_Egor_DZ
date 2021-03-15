"""
5. Реализовать функцию get_jokes(), возвращающую n шуток,
сформированных из трех слов, взятых из трёх списков (по одному слову из каждого списка):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
 get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
слов в шутках (когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?
"""
from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
how_many_jokes = int(input('Сколько шуток мы хотим?'))


def get_jokes(n):
    """
    Функция печатает n шуток
    :param n: число шуток формируемых из списка
    :return:
    """
    for i in range(n):
        a = choice(nouns)
        b = choice(adverbs)
        c = choice(adjectives)
        print(f'{a} {b} {c}')


get_jokes(how_many_jokes)

"""
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
слов в шутках (когда каждое слово можно использовать только в одной шутке)?
->  Самостоятельно не придумал как реализовать запрет повтора слов.

Сможете ли вы сделать аргументы именованными?
->  Если мы создаём переменную которая задает количество шуток и передаём её в функцию - то да.

то что написано ниже уже осмыслял при разборе Вашего кода с репозитория  

"""


def get_jokes2(n, unique=False):
    noun = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverb = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjective = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke_list = []

    if unique:
        n = min(len(noun), len(adverb), len(adjective))

    for i in range(n):
        x = choice(noun)
        y = choice(adverb)
        z = choice(adjective)
        joke = f'{x} {y} {z}'
        joke_list.append(joke)

        if unique:
            noun.remove(x)
            adverb.remove(y)
            adjective.remove(z)

    return joke_list


print(get_jokes2(5, unique=False))
print(get_jokes2(5, unique=True))