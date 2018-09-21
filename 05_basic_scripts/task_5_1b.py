# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#Решение
from sys import argv


ip , mask = argv[1:]
#ip = input('Введите IP-сеть в формате x.x.x.x/yy:    ')
#a = ip.split('/')
a1 = ip.split('.')
b = [int(vlan) for vlan in a1]
b[0] = '{:08b}'.format(b[0])
b[1] = '{:08b}'.format(b[1])
b[2] = '{:08b}'.format(b[2])
b[3] = '{:08b}'.format(b[3])
m_bin = '1' * int(mask) + '0' * (32 - int(mask))
m0 = int(m_bin[0:8], 2)
m1 = int(m_bin[8:16], 2)
m2 = int(m_bin[16:24], 2)
m3 = int(m_bin[24:32], 2)
b_net_bin = bin(int(m_bin, 2) & int(''.join(b), 2))[2:].zfill(32)
b_net_0 = int(b_net_bin[0:8], 2)
b_net_1 = int(b_net_bin[8:16], 2)
b_net_2 = int(b_net_bin[16:24], 2)
b_net_3 = int(b_net_bin[24:32], 2)
print('Network:' + '\n' + '{:<10} {:<10} {:<10} {:<10}'.format(b_net_0, b_net_1, b_net_2, b_net_3))
print('{:<10} {:<10} {:<10} {:<10}'.format(b_net_bin[0:8], b_net_bin[8:16], b_net_bin[16:24], b_net_bin[24:32]))
print ('\n')
print('Mask : ')
print('/' + mask)
print('{:10} {:10} {:10} {:10}'.format(str(m0), str(m1), str(m2), str(m3)))
print('{:10} {:10} {:10} {:10}'.format(m_bin[0:8], m_bin[8:16], m_bin[16:24], m_bin[24:32]))
