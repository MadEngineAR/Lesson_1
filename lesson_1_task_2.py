"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


# Сложность O(n). Цикл for in
def min_value_in_list(lst):
    min_value = 0
    for j in range(len(lst) - 1):  # O(n)
        if lst[j] < lst[j + 1]:  # O(1)
            min_value = lst[j]  # O(1)
            lst[j + 1] = lst[j]  # O(1)
        elif lst[len(lst) - 1] < min_value:  # O(1)
            min_value = lst[len(lst) - 1]  # O(1)
    return min_value  # O(1)


# Сложность O(n^2). Цикл for in c удалением элеметов.
def min_value_in_list1(lst):
    min_value = lst[0]
    for el in lst:
        if el < min_value:
            min_value = el
            del lst[lst.index(el)]
    return min_value


lst1 = [2, 6, 5, 8, 10]
lst2 = [2, 1, 5, 8, 1]
print(min_value_in_list(lst1))
print(min_value_in_list1(lst2))
