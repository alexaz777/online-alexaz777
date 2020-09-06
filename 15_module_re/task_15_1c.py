# -*- coding: utf-8 -*-
'''
Задание 15.1c

Проверить работу скрипта из задания 15.1 и регулярного выражения из задания 15.1a или 9.1b
на выводе sh ip int br из файла sh_ip_int_br_switch.txt.

Если, в результате выполнения скрипта, были выведены не только строки
с интерфейсами 0/1 и 0/3, исправить регулярное выражение.
В регулярном выражении по-прежнему должно быть не более 7 символов.

В результате, должны выводиться только строки с интерфейсами 0/1 и 0/3.

В этом файле нужно написать только регулярное выражение.

'''
# Решение
import re
from sys import argv


file, regex = argv[1:]
#regex = '/1 |/3 '
#file = '/home/python/online-alexaz777/15_module_re/sh_ip_int_br_switch.txt'

with open(file) as f:
    for line in f:
         match = re.search(regex, line)
         if match:
            print(line)




#regex = '/1 |/3 '
