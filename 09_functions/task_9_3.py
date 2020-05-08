# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#Решение

def get_int_vlan_map(cfg_file):
    with open(cfg_file) as f:
        result = {}
        for line in f:
            if line.startswith('interface'):
                int = line.split()[-1]
            elif (' access vlan') in line:
                vlan = line.split()[-1]
                result[int] = vlan
    with open(cfg_file) as f:
        result1 = {}
        for line in f:
            if line.startswith('interface'):
                int = line.split()[-1]
            elif (' allowed vlan') in line:
                vlans = line.split()[-1]
                result1[int] = vlans
    return result, result1

a = get_int_vlan_map('/home/python/online-alexaz777/09_functions/config_sw1.txt')

print(a)

