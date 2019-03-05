# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''
#Решение
from tabulate import tabulate

list_reach = ['10.1.1.1', '10.1.1.2']
list_unreach = ['10.1.1.7', '10.1 1 8', '10.1.1.9', '10.1.1.10']

def ip_table(list_reach, list_unreach):
    list_ip_addresses = {'Reachable': list_reach, 'Unreachable': list_unreach}
    result = tabulate(list_ip_addresses, headers='keys')
    return result


if	__name__	==	"__main__":
    result = ip_table(list_reach, list_unreach)
    print(result)
