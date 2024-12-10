# Даны списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
# 1. Генераторная сборка для разницы длин строк, если их длины не равны
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))
# 2. Генераторная сборка для сравнения длин строк в одинаковых позициях
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
# Преобразуем генераторы в списки и выводим результаты
print(list(first_result))
print(list(second_result))

# first_result: Генераторная сборка, которая использует функцию zip для объединения элементов
# из двух списков first и second. Если длины строк не равны, вычисляется разница их длин и
# добавляется в генератор.
#
# second_result: Генераторная сборка, которая не использует zip. Вместо этого она применяет
# функции range и len для перебора индексов строк в обоих списках. Для каждой пары строк на
# одинаковой позиции проверяется, равны ли их длины, и результат (True или False) добавляется
# в генератор.
#
# Пример вывода:
# [1, 2]
# [False, False, True]