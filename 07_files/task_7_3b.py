# -*- coding: utf-8 -*-
'''
Задание 7.3b5

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#Решение
vlan_number = input('Введите номер VLAN: ')

result = []
#vlans = []

with open('/home/python/online-alexaz777/07_files/CAM_table.txt', 'r') as f:
    for line in f:
        if '.' and '.'  in line:
            result.append(line.replace('DYNAMIC     ', ''))
#           vlans.append(line[0:4])
#            vlans_m = set(vlans)
#            vlans_l = list(vlans_m)
        else:
            continue
#for vlan in vlans_l:
for line1 in result:
    if vlan_number in line1:
            print(line1.rstrip())
    else:
        continue
