"""
3. Реализовать базовый класс Employee (сотрудник).
определить атрибуты: name (имя), surname (фамилия), которые должны передаваться при создании экземпляра Employee;
создать класс Position (должность) с аттрибутами employee (сотрудник/Employee), position (должность/str),
income (вознаграждение/dict) - атрибуты также задаются при создании экземпляра класса;
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus};
в классе Position реализовать методы получения полного имени сотрудника get_full_name() и дохода с учётом премии
get_total_income() (wage + bonus);
проверить работу примера на реальных данных: создать экземпляры классов Employee, Position,
вывести на экран имя сотрудника, его должность и вознаграждение сотрудника, используя методы класса Position.
"""

class Employee:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Position(Employee):
    _income = {"wage": 100, "bonus": 200}

    def __init__(self, name, surname, position):
        super().__init__(name, surname)
        self.position = position


    def get_full_name(self):
        return  f'{self.name} {self.surname} на должности {self.position}'

    def get_total_income(self):
        total_income = self._income["wage"] + self._income["bonus"]
        return  f'зарплата с бонусом составляет {total_income} тугриков'


comrade = Position('Егор', 'Остроумов', 'инженер')

print(comrade.get_full_name())
print(comrade.get_total_income())
