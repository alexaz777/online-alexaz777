# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''
#Решение
import subprocess

list_ip_addresses = ['217.195.65.9-10', '195.144.224.2-4', '192.168.9.14 - 192.168.9.17', '192.168.9.30-192.168.9.33', '1.1.1.1']

def check_ip_availability(list_ip_addresses):
    for ip_addr in list_ip_addresses:
        if '-' in ip_addr:
            if ip_addr.count('.') == 3:
                a = ip_addr.split('.')
                a3 = a[3].split('-')
                list1 = [str(a[0] + '.' + a[1] + '.' + a[2] + '.') + str(i) for i in range(int(a3[0]), int(a3[1])+1)]
                list_ip_addresses = list_ip_addresses + list1
            elif ip_addr.count('.') == 6:
                b = ip_addr.split('-')
                b1 = b[0].split('.')
                b2 = b[1].split('.')
                list2 = [str(b1[0] + '.' + b1[1] + '.' + b1[2] + '.') + str(i) for i in range(int(b1[3]), int(b2[3]) +1)]
                list_ip_addresses = list_ip_addresses + list2
        else:
            continue
    list_del = []
    for ip in list_ip_addresses:
        if '-' in ip:
            list_del.append(ip)
        else:
            continue
    list_ip_addresses = list(set(list_ip_addresses) - set(list_del))
    Alive = []
    Unreachable = []
    for ip_address in list_ip_addresses:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip_address], stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL)
        if reply.returncode == 0:
             Alive.append(ip_address)
        else:
             Unreachable.append(ip_address)
    return Alive, Unreachable

if __name__ == "__main__":
    result = check_ip_availability(list_ip_addresses)
    print('Alive' + str(result[0]))
    print('Unreachable' + str(result[1]))

