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
        config = f.readlines()
        for line in config:
            if line.startswith('interface'):
                int = line.split()
            elif (' access vlan') in line:
                vlan = line.split()
                result1 = {int[1]: vlan[3]}
                result.update(result1)
    with open(cfg_file) as f:
        result3 = {}
        config1 = f.readlines()
        for line in config1:
            if line.startswith('interface'):
                int = line.split()
            elif (' allowed vlan') in line:
                vlans = line.split()
                result2 = {int[1]: [vlans[4]]}
                result3.update(result2)
    return result, result3

