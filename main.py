# Задание 1. one hot
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это
# сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

# Решение

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
# Генерация DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
# Создание one-hot кодирования
unique_values = data['whoAmI'].unique() # Находим уникальные значения
one_hot = pd.DataFrame()
for value in unique_values:
    one_hot[value] = (data['whoAmI'] == value).astype(int)
# Объединение one-hot кодирования с исходным DataFrame (опционально)
data = pd.concat([data, one_hot], axis=1)
print(data.head())

# Задание 2. Анализ расходов по возрасту.
# Постройте линейный график, где по оси X будет отображаться возраст (age), а по оси
# Y — балл по расходам (spending_score). Этот график поможет визуализировать, какие
# изменяются расходы в зависимости от возраста сотрудников. Проанализируйте тренды
# и выявите возможные закономерности.


# Загрузка данных
df = pd.read_csv('data.csv')
# Проверка названий столбцов
print(df.columns)
sns.lineplot(x='age', y='spending_score', data=df)
plt.title('Age vs Spending Score')
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.show()

# Задание 3. Взаимосвязь между зарплатой и бонусами
# Создайте точечный график, где по оси X будет отображаться зарплата (salary), а по
# оси Y — бонусы (bonus). Размер точек на графике должен быть пропорционален
# количеству лет в компании (years_at_company). Этот график позволит исследовать
# взаимосвязь между зарплатой и бонусами и оценить влияние стажа на размер
# бонусов.

# Загрузка данных из CSV-файла
df = pd.read_csv('data.csv')
# Создание точечного графика с использованием Seaborn
# Ось X: зарплата (salary)
# Ось Y: бонусы (bonus)
# Размер точек пропорционален количеству лет в компании (years_at_company)
sns.scatterplot(x='salary', y='bonus', size='years_at_company', data=df)
# Настройка заголовка графика
plt.title('Salary vs Bonus with Years at Company')
# Настройка меток осей
plt.xlabel('Salary')
plt.ylabel('Bonus')
# Отображение графика
plt.show()

