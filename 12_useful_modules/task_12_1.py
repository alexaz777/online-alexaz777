# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#Решение
import subprocess

list_ip_addresses = ['192.168.9.4', "192.168.9.7", '192.168.9.8', '192.168.9.14', '192.168.9.16']

def check_ip_addresses(list_ip_addresses):
    Alive = []
    Unreachable = []
    for ip_addr in list_ip_addresses:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip_addr], stdout= subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if reply.returncode == 0:
            Alive.append(ip_addr)
        else:
            Unreachable.append(ip_addr)
    return Alive, Unreachable


if __name__ == "__main__":
    result = check_ip_addresses(list_ip_addresses)
    print('List_ip_addreses' + str(list_ip_addresses))
    print('Alive'+ str(result[0]))
    print('Unreachable' + str(result[1]))

