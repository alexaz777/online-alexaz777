# -*- coding: utf-8 -*-
'''
Задание 15.3b

Проверить работу функции parse_cfg из задания 15.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 15.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
#Решение
import re
from pprint import pprint

def parse_cfg(filename):

    regex = 'interface (?P<intf2>\S+)\n +ip address (?P<ip1>\S+)+ +(?P<mask1>\S+)\s+ +ip address (?P<ip2>\S+)+ +(?P<mask2>\S+) secondary''|interface (?P<intf>\S+)(.*\n){1,5} +ip address (?P<ip>\S+)+ +(?P<mask>\S+)'

    result = {}

    with open(filename) as f:
        match_iter = re.finditer(regex, f.read())
        for match in match_iter:
            if match:
                intf = match.group('intf')
                intf2 = match.group('intf2')
                ip = match.group('ip')
                ip1 = match.group('ip1')
                result[intf] = ip
                ip2 = match.group('ip2')
                mask = match.group('mask')
                mask1 = match.group('mask1')
                mask2 = match.group('mask2')
                for item in match.groups():
                  if ip2 != None and mask2 != None:
                     result[intf2] = tuple([ip1, mask1]), tuple([ip2, mask2])
                  else:
                     result[intf] = tuple([ip, mask])
        del(result[None])

    return result





print(parse_cfg('/home/python/online-alexaz777/15_module_re/config_r2.txt'))

##'|ip address (?P<ip2>\S+)+ +(?P<mask2>\S+) secondary'