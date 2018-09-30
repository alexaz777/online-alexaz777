# -*- coding: utf-8 -*-
'''
Задание 5.4

Найти индекс последнего вхождения элемента.

Например, для списка num_list, число 10 последний раз встречается с индексом 4; в списке word_list,
 слово 'ruby' последний раз встречается с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в конкретном списке) и
проверить на двух списках, которые указаны и на разных элементах.

Для этого надо запросить у пользователя сначала ввод числа из списка num_list и затем вывести
индекс его последнего появления в списке. А затем аналогично для списка word_list.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = [
    'python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl'
]
#Решение

a = ','.join([str(vlan) for vlan in num_list])
print('Введите число из списка' + '(' + a +')' + ':')
b = input()
number_digits = a.count(',')
num_list.reverse()
index = num_list.index(int(b))
print('Индекс последнего появления числа в списке = ' + str(number_digits - index))

word_list = [
    'python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl'
]
c = ','.join(word_list)
print('Введите слово из списка' + '(' + c +')' + ':')
d = input()
number_words = c.count(',')
word_list.reverse()
index_w = word_list.index(d)
print('Индекс последнего появления слова в списке = ' + str(number_words - index_w))




