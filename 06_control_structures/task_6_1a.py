# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#Решение
a = input('Введите IP-адрес в формате x.x.x.x, где x число от 0 до 255: ')
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
else:
    print('Incorrect IPv4 format')


