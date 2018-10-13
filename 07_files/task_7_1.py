# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#Решение
with open('/home/python/online-alexaz777/07_files/ospf.txt', 'r')	as	f:
    for line in f:
        a = line.split()
        print('')
        print('Protocol:              ' + '{:20}'.format(a[0]).replace('O' , 'OSPF'))
        print('Prefix:                ' + '{:20}'.format(a[1]))
        print('AD/Metric:             ' + '{:20}'.format(a[2].strip('[]')))
        print('Next-Hop:              ' + '{:20}'.format(a[4]))
        print('Outbound Interface:    ' + '{:20}'.format(a[5]))


