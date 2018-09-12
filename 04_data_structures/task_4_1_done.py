# -*- coding: utf-8 -*-
'''
Задание 4.1

Обработать строку NAT таким образом,
чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#NAT = 'ip nat inside source list ACL interface FastEthernet0/1 overload'

#Solution
NAT = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
d = NAT.replace ('Fast' , 'Gigabit')
print (d)
print ('End of programm task_4_1.py')


 
