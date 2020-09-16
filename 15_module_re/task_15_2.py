# -*- coding: utf-8 -*-
'''
Задание 15.2

Создать функцию return_match, которая ожидает два аргумента:
* имя файла, в котором находится вывод команды show
* регулярное выражение

Функция должна обрабатывать вывод команды show построчно и возвращать список подстрок,
которые совпали с регулярным выражением (не всю строку, где было найдено совпадение,
а только ту подстроку, которая совпала с выражением).

Проверить работу функции на примере вывода команды sh ip int br (файл sh_ip_int_br.txt).
Вывести список всех IP-адресов из вывода команды.

Соответственно, регулярное выражение должно описывать подстроку с IP-адресом (то есть, совпадением должен быть IP-адрес).


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
#Решение
import re


regex = ('\d+\.\d+\.\d+\.\d+')

result = []

def return_match(filename, regex):
    with open(filename) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                ip = match.group()
                result.append(ip)
    return result


print(return_match('/home/python/online-alexaz777/15_module_re/sh_ip_int_br.txt', regex))