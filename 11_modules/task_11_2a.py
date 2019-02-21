# -*- coding: utf-8 -*-
'''
Задание 11.2a

С помощью функции parse_cdp_neighbors из задания 11.1
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt


Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
#Решение
from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology

result = {}
result1 = {}
file_name = ['/home/python/online-alexaz777/11_modules/sw1_sh_cdp_neighbors.txt',
             '/home/python/online-alexaz777/11_modules/sh_cdp_n_r1.txt',
             '/home/python/online-alexaz777/11_modules/sh_cdp_n_r2.txt',
             '/home/python/online-alexaz777/11_modules/sh_cdp_n_r3.txt']
for file in file_name:
    with open(file, 'r') as f:
        sh_cdp_neighbors = f.readlines()
        result1 = parse_cdp_neighbors(sh_cdp_neighbors)
        list_keys = list(result.keys())
        list_values = list(result1.values())
        for double in list_keys:
            if double in list_values:
                del(result[double])
        result.update(result1)

draw_topology(result, '/home/python/online-alexaz777/11_modules/img/task_11_2a_topology')
