# -*- coding: utf-8 -*-
'''
Задание 15.4a

Создать функцию convert_to_dict, которая ожидает два аргумента:
* список с названиями полей
* список кортежей с результатами отработки функции parse_sh_ip_int_br из задания 15.4

Функция возвращает результат в виде списка словарей (порядок полей может быть другой):
[{'interface': 'FastEthernet0/0', 'status': 'up', 'protocol': 'up', 'address': '10.0.1.1'},
 {'interface': 'FastEthernet0/1', 'status': 'up', 'protocol': 'up', 'address': '10.0.2.1'}]
   
Проверить работу функции на примере файла sh_ip_int_br_2.txt:
* первый аргумент - список headers
* второй аргумент - результат, который возвращает функции parse_show из прошлого задания.

Функцию parse_sh_ip_int_br не нужно копировать.
Надо импортировать или саму функцию, и использовать то же регулярное выражение,
что и в задании 15.4, или импортировать результат выполнения функции parse_show.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#Решение

import re
from pprint import pprint
from task_15_4_1 import parse_sh_int_br

headers = ['interface', 'address', 'status', 'protocol']
table = parse_sh_int_br('/home/python/online-alexaz777/15_module_re/sh_ip_int_br.txt')
table1 = parse_sh_int_br('/home/python/online-alexaz777/15_module_re/sh_ip_int_br_2.txt')


def convert_to_dict(headers, table):
    regex = '[(]\S(?P<int>\w+\d+(\S\d+)?)\S+[, ]\S(?P<addr>[\d.]+|unassigned)\S[,]\s+\S(?P<stat>\w+(\s\w+)?)\S[,]\s+\S(?P<prot>\w+)\S+'

    regex = re.sub('int', headers[0], regex)
    regex = re.sub('addr', headers[1], regex)
    regex = re.sub('stat', headers[2], regex)
    regex = re.sub('prot', headers[3], regex)
    result1 = {}
    result =[]
    result333 = re.finditer(regex, str(table))
    for match in result333:
            if match:
                result1 = match.groupdict()
                result.append(result1)

    return result



if __name__ == "__main__":
    result = convert_to_dict(headers, table1)
    print(result)


