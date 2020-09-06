# -*- coding: utf-8 -*-
'''
Задание 15.1a

Напишите регулярное выражение, которое отобразит строки
с интерфейсами 0/1 и 0/3 из вывода sh ip int br.

Проверьте регулярное выражение, используя скрипт, который был создан в задании 15.1,
и файл sh_ip_int_br.txt.

В этом файле нужно написать только регулярное выражение.

'''
# Решение
import re
from sys import argv


file, regex = argv[1:]
#regex = '0/1|0/3'
#file = '/home/python/online-alexaz777/15_module_re/sh_ip_int_br.txt'

with open(file) as f:
    for line in f:
         match = re.search(regex, line)
         if match:
            print(line)






