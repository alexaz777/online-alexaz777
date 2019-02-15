# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#Решение
#from sys import argv

#file_name = '/home/python/online-alexaz777/11_modules/sw1_sh_cdp_neighbors.txt'
def parse_cdp_neighbors(file_name):
     result = {}
     result1 = {}
     with open(file_name, 'r') as f:
         for line in f:
             line = line.split()
             if line and '>show' in line[0]:
                 i = line[0].find('>')
                 loc_dev = line[0][:i]
             elif line and line[2][0].isdigit() and  line[4] == 'R' :
                 rem_dev, loc_int, loc_int_number, holdt, _, _, _, _, rem_int, rem_int_number = line
                 result1[loc_dev, loc_int + loc_int_number] = rem_dev, rem_int + rem_int_number
             elif line and line[2][0].isdigit() and line[4] == 'S':
                 rem_dev, loc_int, loc_int_number, holdt, _, _, _, rem_int, rem_int_number = line
                 result1[loc_dev, loc_int + loc_int_number] = rem_dev, rem_int + rem_int_number
         result.update(result1)
     return result
