# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
a = input('Введите IP-адрес в формате x.x.x.x, где x число от 0 до 255: ')

address_correct = False

while not address_correct:
    a1 = a.split('.')
    if a.count('.') == 3 and a1[0].isdigit() and a1[1].isdigit() and a1[2].isdigit() and a1[3].isdigit()\
            and int(a1[0]) <= 255 and int(a1[1]) <= 255 and int(a1[2]) <= 255 and int(a1[3]) <= 255:
        print('Correct IPv4 address')
        if int(a1[0]) == 255 and int(a1[1]) == 255 and int(a1[2]) == 255 and int(a1[3]) == 255:
            print('local broadcast')
        elif int(a1[0]) == 0 and int(a1[1]) == 0 and int(a1[2]) == 0 and int(a1[3]) == 0:
            print('unassigned')
        elif int(a1[0]) <= 223:
            print('unicast')
        elif int(a1[0]) >= 224 and int(a1[0]) <= 239:
            print('multicast')
        else:
            print('unused')
        address_correct = True
    else:
        print('Incorrect IPv4 format')
        a = input('введите IP-адрес еще раз: ')


