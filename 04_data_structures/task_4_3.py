# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки CONFIG список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'

#Решение
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
d = CONFIG.split()
print (d[-1].split(',')) 
