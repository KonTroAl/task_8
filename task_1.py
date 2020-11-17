"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""

from collections import Counter, deque


def char_frequency(a):
    frequency = Counter(a)
    sorted_char = deque(sorted(frequency.items(), key=lambda item: item[1]))
    if len(sorted_char) != 1:
        while len(sorted_char) > 1:
            val = sorted_char[0][1] + sorted_char[1][1]
            my_val_dict = {
                0: sorted_char.popleft()[0],
                1: sorted_char.popleft()[0]
            }
            for b, c in enumerate(sorted_char):
                if val > c[1]:
                    continue
                else:
                    sorted_char.insert(b, (my_val_dict, val))
                    break
            else:
                sorted_char.append((my_val_dict, val))
    else:
        val = sorted_char[0][1]
        my_val_dict = {
            0: sorted_char.popleft()[0],
            1: None
        }
        sorted_char.append((my_val_dict, val))
    return sorted_char[0][0]


my_code = dict()


def my_haffman_code(struct, elem=''):
    if not isinstance(struct, dict):
        my_code[struct] = elem
    else:
        my_haffman_code(struct[0], elem=f'{elem}0')
        my_haffman_code(struct[1], elem=f'{elem}1')


my_str = "beep boop beer!"

# print(char_frequency(my_str))
my_haffman_code(char_frequency(my_str))
# print(my_haffman_code(char_frequency(my_str)))
print(my_code)
for i in my_str:
    print(my_code[i], end=" ")
print()

# my_str_in = "Введите строку для кодирования по Хаффамну: "
