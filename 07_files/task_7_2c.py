# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

#Решение
from sys import argv

file_name_in, file_name_out = argv[1:]
i = ','.join(ignore).count(',')
with open(file_name_in, 'r')	as	src:
    with open(file_name_out, 'w') as dest:
       for line in src:
            if [word for word in ignore if word in line]:
                continue
            else:
                dest.write(line)

