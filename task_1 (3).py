# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие
# только чисел. Проверить работу исключения на реальном примере. Запрашивать у пользователя данные
# и заполнять список необходимо только числами. Класс-исключение должен контролировать типы данных
# элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам
# не остановит работу скрипта, введя, например, команду «stop». При этом скрипт завершается,
# сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю
# ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться  .

class My_Error_list(Exception):
    pass


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


my_list = []
while True:
    try:
        numerical_list_element = input('Please input only numerical element of list ("stop" - command break):')
        if numerical_list_element == 'stop':
            print(" Operation was stop!")
            print(f"Operation was stop! The result - list: {my_list}")
            break
        if is_number(numerical_list_element) == True:
            my_list.append(float(numerical_list_element))
        else:
            raise My_Error_list('Error! Numerical element only!')

    except My_Error_list as err:
        print(err)
