# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
#Решение
from sys import argv

file_name = argv[1]
i = ','.join(ignore).count(',')
with open(file_name, 'r')	as	f:
    for line in f:
        if line.startswith('!'):
            continue
        elif ignore[0] in line:
            continue
        elif ignore[1] in line:
           continue
        elif ignore[2] in line:
           continue
        else:
           print(line.rstrip())
