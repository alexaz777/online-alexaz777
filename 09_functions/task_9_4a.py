# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#Решение
def config_to_dict(cfg_file):
    result = {}
    with open(cfg_file) as f:
        for command in f:
            if command.startswith('!') or command.startswith(' !'):
                continue
            elif ignore_command(command, ignore):
                continue
            elif not command.startswith(' '):
                d_key = command.rstrip()
                d_value = []
                result[d_key] = d_value
            elif command.startswith(' ') and not '  ' in command:
                d_value.append(command.rstrip())
                result[d_key] = d_value
                d_value_3 = []
            elif command.startswith(' ') and  command[0:2] == '  ' in command:
                d_value_3.append(command.rstrip())
                result1 = {d_key: {key: [] for key in d_value}}
                result1[d_key] [d_value[-1]] = d_value_3
                result.update(result1)
    return result


ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)


ignore = ['duplex', 'alias', 'Current configuration']

