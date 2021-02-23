# ЗАДАНИЕ 4
#
# Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран
# отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ..
# 100 процентов


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
word_list = ['процент', 'процента', 'процентов']
user_value = int(input('Сколько процентов?'))

if user_value // 10 == 1:           #от 10 до 19
    print(user_value, word_list[2])
elif user_value // 10 == 10:        #100
    print(user_value, word_list[2])
elif user_value % 10 == number_list[0]:
    print(user_value, word_list[0])
elif user_value % 10 in number_list [1:4]:
    print(user_value, word_list[1])
else:
    print(user_value, word_list[2])
