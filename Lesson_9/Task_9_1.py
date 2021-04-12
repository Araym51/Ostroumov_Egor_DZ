"""1. Создать класс TrafficLight (светофор).
определить у него один приватный атрибут color (цвет) и метод get_current_signal() (получить текущий цвет);
после создания экземпляра светофора, он запускает режим смены сигналов с разной длительностью: красный (3 сек),
жёлтый (1 сек), зелёный (3 сек);
переключение идет циклично в порядке красный-жетлый-зеленый-красный-жетлый-зеленый-красный-...
проверить переключение режимов работы светофора, опрашивая в цикле текущее состояние светофора с интервалом 0.5 секунды,
используя метод get_current_signal()."""

from time import sleep


class TrafficLight:
    color = ''

    def current_signal(self):
        i = 0
        while i == 0:
            self.color = 'red'
            print(self.color)
            sleep(3)
            self.color = 'yellow'
            print(self.color)
            sleep(1)
            self.color = 'green'
            print(self.color)
            sleep(3)


def get_current_signal(value):
    i_2 = 0
    while i_2 == 0:
        print(value)
        sleep(0.5)


b = TrafficLight()
get_current_signal(b.current_signal())
