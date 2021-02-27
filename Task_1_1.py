# ЗАДАНИЕ 1
# Человеко-ориентированное представление интервала времени Спросить у  пользователя
# размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:
# 1) до минуты: <s> сек;
# 2) до часа: <m> мин <s> сек;
# 3) до суток: <h> час <m> мин <s> сек;
# 4) сутки или больше: <d> дн <h> час <m> мин <s> сек 86400
#
# Например, если пользователь введет 4567 секунд, вывести:
# 1 час 16 мин 7 сек


array = []
user_value = int(input("Введите секунды"))
if user_value >= 86400 :
    days = user_value // 86400
    array.append(days)
    user_value = user_value % 86400
    hours = user_value // 3600
    array.append(hours)
    user_value = user_value % 3600
    minutes = user_value // 60
    array.append(minutes)
    seconds = user_value % 60
    array.append(seconds)
    print(array[0], ' суток', array[1], ' часов', array[2], ' минут', array[3], 'секунд')
elif user_value < 86400 and user_value >= 3600:
    hours = user_value // 3600
    array.append(hours)
    user_value = user_value % 3600
    minutes = user_value // 60
    array.append(minutes)
    seconds = user_value % 60
    array.append(seconds)
    print( array[0], ' часов', array[1], ' минут', array[2], 'секунд')
elif user_value < 3600 and user_value >= 60:
    minutes = user_value // 60
    array.append(minutes)
    seconds = user_value % 60
    array.append(seconds)
    print( array[0], ' минут', array[1], 'секунд')
else:
    seconds = user_value % 60
    array.append(seconds)
    print( array[0], 'секунд')