"""2. Реализовать класс Road (дорога).
определить защищенные атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
определить внутри класса приватную константу масса квадратного метра асфальта толщиной 1 см.
определить метод расчёта массы асфальта get_asphalt_mass(height), необходимого для покрытия всей дороги
толщиной height см;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т."""


class Road:
    lenght = ''
    width = ''
    square_mass = ''
    height = ''

    def get_asphalt_mass(lenght, width, square_mass,height ):
        asphalt_mass = int((lenght * width * square_mass * height) / 1000)
        print(f'{asphalt_mass} тонн')

a = Road.get_asphalt_mass(20, 5000, 25, 5)
print(a)