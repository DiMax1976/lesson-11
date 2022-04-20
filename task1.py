#
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.



class Datas:

    def __init__(self, day, mounth, year):
        self.day = day
        self.mounth = mounth
        self.year = year

    data_list = []

    @classmethod
    def modify_str(cls, my_string):
        pattern = re.compile('(?P<day>.+)-(?P<mounths>.+)-(?P<year>.+)')
        data1 = pattern.finditer(my_string)
        for res in data1:
            my_dict = res.groupdict()
        day = int(my_dict.get('day'))
        mounth = int(my_dict.get('mounths'))
        year = int(my_dict.get('year'))
        return cls(day, mounth, year)

    @staticmethod
    def get_data(self):
        if self.mounth > 12 or self.mounth <= 0:
            check_mounth = "Mounth not valid,"
        else:
            check_mounth = "Mounth is OK,"

        if self.year > 2022:
            check_year = "Year not valid"
        else:
            check_year = "Year is OK"
        return f"{self.mounth} {check_mounth} {self.year} {check_year}"


test = Datas.modify_str("25-08-1976")
test2 = Datas.modify_str("25-13-2025")
test3 = Datas.modify_str("25-0-1976")
print(test.day, test.mounth, test.year)
print(test.get_data(test))
print(test2.get_data(test2))
print(test3.get_data(test3))
