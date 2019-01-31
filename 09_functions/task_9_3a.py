# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#Решение
def get_int_vlan_map(cfg_file):
    with open(cfg_file) as f:
        result = {}
        for line in f:
            if line.startswith('interface'):
                int = line.split()[-1]
            elif (' mode access') in line:
                result[int] = '1'
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
