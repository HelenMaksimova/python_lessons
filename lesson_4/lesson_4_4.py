# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

from random import randint

start_list = [randint(1, 100) for _ in range(20)]

print(f'Начальный список:\n{start_list}')

finish_list = [elem for elem in start_list if start_list.count(elem) == 1]

print(f'Список уникальных элементов:\n{finish_list}')
