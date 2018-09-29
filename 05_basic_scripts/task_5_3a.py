# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
#Решение
question = {'access':'Enter VLAN number: ', 'trunk':'Enter allowed VLANs: '}
mode = input('Enter interface mode (access/trunk): ')
print(question.get(mode))
vlan = input()
interface = input('Enter interface type and number: ')
a = '\n'.join(access_template).format(vlan)
b = '\n'.join(trunk_template).format(vlan)
print('\n' + '-' * 30)
print('interface {}'.format(interface))
switch_mode = {'access':a , 'trunk':b} 
print(switch_mode[mode])
