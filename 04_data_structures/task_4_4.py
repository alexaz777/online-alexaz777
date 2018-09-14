# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

#Решение
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
d1 = command1.split()
d2 = command2.split()
vlans1 = d1[-1].split(',')
vlans2 = d2[-1].split(',')
vlans1_set = set(int(vlan) for vlan in vlans1)
vlans2_set = set(int(vlan) for vlan in vlans2)
list(vlans1_set & vlans2_set)
print(list(vlans1_set & vlans2_set)) 
 

