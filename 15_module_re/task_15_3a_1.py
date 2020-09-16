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


    result = {}

    with open(filename) as f:
        for line in f:
            if line.startswith('interface'):
                int = re.search('interface (\S+)', line).group(1)
            elif line.startswith(' ip address '):
                ip_addr = re.findall('ip address (\S+) (\S+)', line)
                result[int] = ip_addr

    return result

print(parse_cfg('/home/python/online-alexaz777/15_module_re/config_r2.txt'))









#regex = 'interface (?P<intf>\S+)(.*\n+){1,5} +(ip address (?P<ip>\S+) (?P<mask>\S+)\n)|(ip address (?P<ip2>\S+) (?P<mask2>\S+) secondary\n)'
#        int = match.group('intf')
#        ip = match.group('ip')
#        ip2 = match.group('ip2')elif line.startswith(' ip address '):
#        mask = match.group('mask')
#        mask2 = match.group('mask2')
#        result1 = [ip, mask]
#        result2 = [ip2, mask2]
#        for item in match.groups():
#            if ip2 == None and mask2 == None:
#                result[int] = tuple(result1)
#            else:
#                result[int] = tuple(result1 + result2)
#    del(result[None])
#print(result)