# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
#Решение
import re



def parse_cfg(filename):
    regex = 'interface (?P<intf>\S+)(.*\n){1,5} +ip address (?P<ip>\S+)+ +(?P<mask>\S+)'

    result = {}

    with open(filename) as f:
        match_iter = re.finditer(regex, f.read())
        for match in match_iter:
            if match:
                intf = match.group('intf')
                ip = match.group('ip')
                mask = match.group('mask')
                result1 = [ip, mask]
                result2 = tuple(result1)
                result[intf] = result2

    return result





print(parse_cfg('/home/python/online-alexaz777/15_module_re/config_r1.txt'))
