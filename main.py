# Задание 1. Новые списки
# Даны три списка:
# 1. floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# 2. names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# 3. numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
# Напишите код, который создаёт три новых списка. Вот их содержимое:
# 1. Каждое число из списка floats возводится в третью степень и округляется
# до трёх знаков после запятой.
# 2. Из списка names берутся только имена минимум из пяти букв.
# 3. Из списка numbers берётся произведение всех чисел.

from functools import reduce
# Исходные списки
floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]
# Применяем функцию map для возведения в третью степень и округления до трех знаков после запятой
map_result = list(map(lambda x: round(x ** 3, 3), floats))
# Применяем функцию filter для выбора имен из пяти и более букв
filter_result = list(filter(lambda name: len(name) >= 5, names))
# Применяем функцию reduce для нахождения произведения всех чисел в списке
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)
# Вывод результатов
print(map_result)
print(filter_result)
print(reduce_result)

# Задача 2. Zip
# Даны список букв (letters) и список цифр (numbers). Каждый список состоит из N
# элементов. Создайте кортежи из пар элементов списков и запишите их в список
# results. Не используйте функцию zip. Решите задачу в одну строку (не считая
# print(results)).
# Примеры списков:
# letters: List[str] = ['a', 'b', 'c', 'd', 'e']
# numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
# Результат работы программы:
# [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

from typing import List, Tuple
# Исходные списки
strings = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Создание списка кортежей, состоящих из пар элементов из обоих списков
results: List[Tuple[str, int]] = list(map(lambda x, y: (x, y),
strings, numbers))
# Вывод результатов
print(results)

# Задача 3. Палиндром
# Используя модуль collections, реализуйте функцию can_be_poly, которая
# принимает на вход строку и проверяет, можно ли получить из неё палиндром.
# Пример кода:
# print(can_be_poly('abcba'))
# print(can_be_poly('abbbc'))
# Результат:
# True
# False

from collections import Counter
def can_be_poly(val: str) -> bool:
    # Создаем счетчик частот символов в строке
    char_counts = Counter(val)
    # Проверяем количество символов с нечетным количеством вхождений
    odd_count = len(list(filter(lambda x: x % 2,
    char_counts.values())))
    # Условие для проверки возможности формирования палиндрома
    return odd_count < 2
print(can_be_poly('eerru')) # Ожидаемый результат: True
print(can_be_poly('abbcba')) # Ожидаемый результат: True
print(can_be_poly('abbbc')) # Ожидаемый результат: False

# Задача 4. Уникальный шифр
# Напишите функцию, которая принимает строку и возвращает количество
# уникальных символов в строке. Используйте для выполнения задачи
# lambda-функции и map и/или filter.
# Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного
# регистра должны считаться одинаковыми.
# Пример:
# message = "Today is a beautiful day! The sun is shining and the birds are
# singing."
# unique_count = count_unique_characters(message)
# print("Количество уникальных символов в строке:", unique_count)
# Вывод: количество уникальных символов в строке — 5.

def count_unique_characters(string):
    # Приводим строку к нижнему регистру, чтобы сделать подсчет регистронезависимым
    lower_string = string.lower()
    # Используем filter для выбора символов, которые встречаются в строке ровно один раз
    unique_chars = list(filter(lambda c: lower_string.count(c.lower()) == 1, lower_string))
    # Выводим уникальные символы (по желанию, можно удалить эту строку)
    print(unique_chars)
    # Возвращаем количество уникальных символов
    return len(unique_chars)
# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
