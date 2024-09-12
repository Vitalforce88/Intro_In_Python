# Набор рекламных данных, показывающих, щёлкнул ли конкретный
# пользователь рекламу на сайте компании или нет. Состоит из двух разных
# файлов: advertising_1.csv, advertising_2.csv. Описание столбцов
# датасета:
# ● Number: Номер пользователя в системе.
# ● Daily Time Spent on Site: Среднее ежедневное время нахождения
# пользователя на сайте в минутах.
# ● Daily Internet Usage: Среднее ежедневное время нахождения
# пользователя в интернете в минутах.
# ● Ad Topic Line: Заголовок рекламного объявления.
# ● Clicked on Ad: Кликнул пользователь на рекламу или нет.

# Задание 1.
# Загрузите таблицу из файла advertising_1.csv и сохраните её в датафрейм
# adv1_df. Укажите в качестве индекса столбец Number. Выведите на экран
# первые десять строк.

#Решение:
import pandas as pd
# вариант 1
adv1_df = pd.read_csv('advertising_1.csv', index_col='Number')
# вариант 2
adv1_df = pd.read_csv('advertising_1.csv')
adv1_df = adv1_df.set_index('Number')
# вариант 3
adv1_df = pd.read_csv('advertising_1.csv')
adv1_df.set_index('Number', inplace=True)
# Отображение первых 10 строк
# вариант 1 (приоритет)
print(adv1_df.head(10))
# вариант 2 (приоритет)
print(adv1_df[:10])
# вариант 3
print(adv1_df.loc[:10 , :])

# Задание 2.
# Выведите размер датафрейма adv1_df и cреднее ежедневное время
# нахождения в интернете пользователя под номером 8.
# Вывод размерности
print(adv1_df.shape)
# вариант 1
print(adv1_df.loc[8, 'Daily Internet Usage'])
# вариант 2
print(adv1_df.iloc[2, 1])

# Задание 3.
# Загрузите таблицу из файла advertising_2.csv и сохраните её в датафрейм
# adv2_df. Укажите в качестве индекса стоблец Number. Выведите на экран
# строки для пользователей с номерами с 533-го по 536-й.

# Загрузка данных
# вариант 1
adv2_df = pd.read_csv('advertising_2.csv', index_col='Number')
# вариант 2
adv2_df = pd.read_csv('advertising_2.csv')
adv2_df = adv2_df.set_index('Number')
# вариант 3
adv2_df = pd.read_csv('advertising_2.csv')
adv2_df.set_index('Number', inplace=True)

# Отображение пользователей с номерами с 533 по 536
# вариант 1
print(adv2_df.loc[533:536])
# вариант 2 (приоритет)
print(adv2_df.loc[533:536, :])
# вариант 3
print(adv2_df.iloc[3:7])