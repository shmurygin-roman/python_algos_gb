"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import namedtuple, defaultdict

"""Решение с использованием namedtuple"""

firms = namedtuple('Firm', 'id name q_1 q_2 q_3 q_4 summ')
firms_list = []

num = int(input('Введите количество предприятий для расчета прибыли: '))
for i in range(1, num+1):
    id = i
    name = input(f'Введите название предприятия # {i}: ')
    q_1, q_2, q_3, q_4 = input('Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала)').split()
    summ = float(q_1) + float(q_2) + float(q_3) + float(q_4)
    firms_list.append(firms._make((id, name, q_1, q_2, q_3, q_4, summ)))
print(firms_list)

avg_profit = (sum([i.summ for i in firms_list]) / len(firms_list))
print(f'Средняя годовая прибыль всех предприятий: {avg_profit}')
list_above_avg = [i.name for i in firms_list if i.summ >= avg_profit]
print(f"Предприятия, с прибылью выше или равно среднего значения: {';'.join(list_above_avg)}")
list_below_avg = [i.name for i in firms_list if i.summ < avg_profit]
print(f"Предприятия, с прибылью ниже среднего значения: {';'.join(list_below_avg)}")


"""Решение с использованием defaultdict"""

firms = defaultdict(list)

num = int(input('Введите количество предприятий для расчета прибыли: '))
for i in range(1, num+1):
    name = input(f'Введите название предприятия # {i}: ')
    profit = [float(i) for i in input('Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): ').split()]
    firms[name] = profit
print(firms)

avg_profit = (sum([sum(i) for i in firms.values()]) / len(firms))
print(f'Средняя годовая прибыль всех предприятий: {avg_profit}')
list_above_avg = [key for key, value in firms.items() if sum(value) >= avg_profit]
print(f"Предприятия, с прибылью выше или равно среднего значения: {';'.join(list_above_avg)}")
list_below_avg = [key for key, value in firms.items() if sum(value) < avg_profit]
print(f"Предприятия, с прибылью ниже среднего значения: {';'.join(list_below_avg)}")

