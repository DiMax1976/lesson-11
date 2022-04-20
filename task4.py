# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class Office_equipment_warehouse:
    def __init__(self, manufacturer, place, division, position):
        self.manufacturer = manufacturer
        self.place = place
        self.division = division
        self.position = position


class Office_equipment():
    def __init__(self, name, type_equipment, price):
        self.name = name
        self.type_equipment = type_equipment
        self.price = price

    def __str__(self):
        return f"{self.name} {self.type_equipment} {self.price}"


class Printer(Office_equipment):
    def __init__(self, name, type_equipment, price, speed_print):
        super().__init__(name, type_equipment, price)
        self.speed_print = speed_print
    def __str__(self):
        return f"Brand: {self.name}, Type of print {self.type_equipment}, Price: {self.price}, Speed of print {self.speed_print}"

class Xerox(Office_equipment):
    def __init__(self, name, type_equipment, price, print_type):
        super().__init__(name, type_equipment, price)
        self.print_type = print_type


class Scaner(Office_equipment):
    def __init__(self, name, type_equipment, price, resolution):
        super().__init__(name, type_equipment, price)
        self.resolution = resolution


bid_printer = Printer("LG", "laser", 25000, 250)
print(bid_printer)