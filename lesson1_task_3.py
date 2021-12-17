"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!"""

company_income_dict = {'Mercedes': 1000, 'BMW': 3000, 'Audi': 2000, 'Toyota': 5000}


"""Вариант 1. Сортировка по значениям. Проход по значениям, проход по ключам
   Сложность O(n^2)"""
# sorted_values = sorted(company_income_dict.values(), reverse=True)[0:3]  # O(n log n) + O(1)
# sorted_dict = {} # O(1)
# for i in sorted_values:  # O(n)
#     for k in company_income_dict.keys():  # O(n)
#         if company_income_dict[k] == i:  # O(1)
#             sorted_dict[k] = company_income_dict[k]  # O(1)
#             break
# print(sorted_dict)

"""Вариант 2. Сортировка по ключам. Проход по ключам
   Сложность O(n)"""
sorted_values = sorted(company_income_dict.values(), reverse=True)[0:3]
sorted_dict1 = {}  # O(1)
sorted_keys = sorted(company_income_dict, key=company_income_dict.get, reverse=True)[0:3]  # O(n log n) + O(1)
for el in sorted_keys:  # O(n)
    sorted_dict1[el] = company_income_dict[el]  # O(1)

print(sorted_dict1)
