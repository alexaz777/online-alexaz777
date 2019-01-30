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
        result5 = {}
        config2 = f.readlines()
        for line in config2:
            if line.startswith('interface'):
                int = line.split()
            elif (' mode access') in line:
                result4 = {int[1]: '1'}
                result5.update(result4)
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
    result5.update(result)
    return result5, result3
