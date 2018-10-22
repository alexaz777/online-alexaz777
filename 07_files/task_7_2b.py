# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

#Решение
from sys import argv

file_name = argv[1]
i = ','.join(ignore).count(',')
with open(file_name, 'r')	as	src:
    with open('config_sw1_cleared.txt', 'w') as dest:
       for line in src:
            if ignore[0] in line:
                continue
            elif ignore[1] in line:
                continue
            elif ignore[2] in line:
                continue
            else:
                dest.write(line)


