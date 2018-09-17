# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

#Решение

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
a = ospf_route.split()
print('Protocol:              ' + '{:20}'.format(a[0]).replace('O' , 'OSPF'))
print('Prefix:                ' + '{:20}'.format(a[1]))
b = a[2]
print('AD/Metric:             ' + '{:20}'.format(b.strip('[]')))
print('Next-Hop:              ' + '{:20}'.format(a[4]))
print('Outbound Interface:    ' + '{:20}'.format(a[5]))
