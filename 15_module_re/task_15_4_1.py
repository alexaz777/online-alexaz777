# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.

'''
#Решение

import re
from pprint import pprint

def parse_sh_int_br(filename):
    regex = '(\S+) +([\d.]+|unassigned) +\w+ +\w+ +(up|down|administratively down) +(up|down)'

    with open(filename) as f:
        result = re.findall(regex, f.read())
    return result


if __name__ == "__main__":
    pprint(parse_sh_int_br('/home/python/online-alexaz777/15_module_re/sh_ip_int_br_2.txt'))



