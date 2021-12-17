"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

"""ВАРИАНТ 1. Сложность О(n^2).
Цикл for el in list O(n). В цикле также есть проверка IN LIST O(n) по ответу пользователя"""


def check_activate():
    dct_lst = dict1.keys()  # O(n)
    login_lst = [el[0] for el in dct_lst]  # O(n)
    answers = ('Y', 'N')  # O(1)
    message = None  # O(1)
    print(f'Введите пожалуйста логин')
    login = input()  # O(1)
    for el in dct_lst:  # O(n)
        if el[0] == login:
            print(f'Пожалуйста введите пароль')
            password = input()
            if password == el[1] and dict1.get(el) == 'activated':  # O(1)
                message = 'Вам разрешен доступ'  # O(1)
            elif password == el[1] and dict1.get(el) == 'not activated':  # O(1)
                print(f'Для доступа к ресурсу пользователю {el[0]} необходимо активировать учетную запись.'
                      f'Желаете это сделать?Введите "Y" если да, "N" если нет')
                answer = input().upper()  # O(1)
                while answer not in answers:  # O(1)
                    print(f'Неправильный ввод данных. Повторите ввод')
                    answer = input().upper()
                if answer == 'Y':  # O(1)
                    dict1[(login, password)] = 'activated'  # O(1)
                    message = 'Вам открыт доступ'  # O(1)
                elif answer in answers and answer == 'N':  # O(1)
                    message = "Вам отказано в доступе"  # O(1)
                else:
                    message = 'Неправильный пароль'  # O(1)
            else:
                message = 'Неправильный пароль'  # O(1)
        elif login not in login_lst:
            message = 'Данный пользователь не зарегистрирован'
    print(message)
    return message


"""ВАРИАНТ 2. Сложность О(n).
Ушел от цикла. Применил множества."""


def check_activate1():
    dct_lst = dict1.keys()  # O(n)
    login_lst = [el[0] for el in dct_lst]  # O(n)
    logins = set(login_lst)
    answers = {'Y', 'N'}  # O(1)
    message = None  # O(1)
    print(f'Введите пожалуйста логин')
    login = input()  # O(1)
    if login not in logins:  # O(1)
        message = 'Данного пользователя нет в базе'  # O(1)
    else:
        print(f'Пожалуйста введите пароль')
        password = input()  # O(1)
        if dict1.get((login, password)) == 'activated':  # O(1)
            message = 'Вам разрешен доступ'  # O(1)
        elif dict1.get((login, password)) == 'not activated':  # O(1)
            print(f'Для доступа к ресурсу пользователю {login} необходимо активировать учетную запись.'
                  f'Желаете это сделать?Введите "Y" если да, "N" если нет')
            answer = input().upper()  # O(1)
            while answer not in answers:  # O(1)
                print(f'Неправильный ввод данных. Повторите ввод')
                answer = input().upper()
            if answer == 'Y':  # O(1)
                dict1[(login, password)] = 'activated'  # O(1)
                message = 'Вам открыт доступ'  # O(1)
            elif answer in answers and answer == 'N':  # O(1)
                message = "Вам отказано в доступе"  # O(1)
        else:
            message = 'Неправильный пароль'  # O(1)
    print(message)
    return message


dict1 = {('Login1', 'Pass1'): 'activated', ('Login2', 'Pass2'): 'not activated',
         ('Login3', 'Pass3'): 'not activated'}
# print(dict1.get(('Login1', 'Pass1')))
check_activate()
# check_activate1()
