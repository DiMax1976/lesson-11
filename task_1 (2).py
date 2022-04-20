# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.
import asyncio
class My_Error_Zero(Exception):
    pass

try:
    in_data=int(input('Enter a divisible number:'))
    divider = int(input('Enter a divider number:'))
    if divider==0:
        raise My_Error_Zero('Only Positive divider!')
except ValueError as err:
    print(err)
except My_Error_Zero as err:
    print(err)
else:
    print(in_data/divider)

100